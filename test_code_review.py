import pytest
from code_review import CodeReview

@pytest.fixture
def reviewer():
    """
    Pytest fixture that creates and returns a CodeReview instance for testing.
    
    Returns:
        CodeReview: An initialized instance of the CodeReview class ready for use in test scenarios.
    """
    return CodeReview()

def test_basic_review(reviewer):
    """
    Test the basic functionality of code review analysis.
    
    Verifies that the `analyze_code` method of the `CodeReview` class returns a list 
    when processing a simple code snippet.
    
    Args:
        reviewer (CodeReview): An instance of the CodeReview class used for code analysis.
    
    Returns:
        None: The method performs an assertion to validate the return type.
    
    Raises:
        AssertionError: If the returned issues are not a list.
    """
    code = """
def hello():
    print('world')
    """
    issues = reviewer.analyze_code(code)
    assert isinstance(issues, list)

def test_syntax_error_detection(reviewer):
    """
    Test the detection of syntax errors in code.
    
    This test verifies that the code review process correctly identifies and flags syntax errors
    with high severity. It checks a code snippet with an intentional syntax error (missing colon
    after function definition) to ensure the analyzer:
    - Generates at least one issue
    - Marks the syntax error as high severity
    - Includes 'Syntax error' in the issue message
    
    Parameters:
        reviewer (CodeReview): An instance of the CodeReview class used for code analysis
    
    Raises:
        AssertionError: If the syntax error is not correctly detected or classified
    """
    code = """
def broken_function()
    print('missing colon')
    """
    issues = reviewer.analyze_code(code)
    assert len(issues) > 0
    assert issues[0]['severity'] == 'high'
    assert 'Syntax error' in issues[0]['message']

def test_long_function_detection(reviewer):
    """
    Test the detection of excessively long functions in code analysis.
    
    This test verifies that the code review process correctly identifies and flags functions 
    that exceed a predefined maximum length threshold.
    
    Parameters:
        reviewer (CodeReview): An instance of the CodeReview class used for code analysis.
    
    Raises:
        AssertionError: If no issue is found indicating that the function is too long.
    
    Example:
        A function with more than 20 repeated lines will trigger a "too long" warning.
    """
    long_function = "def long_func():\n" + "    print('line')\n" * 25
    issues = reviewer.analyze_code(long_function)
    assert any(
        issue['message'].startswith("Function 'long_func' is too long")
        for issue in issues
    )

def test_variable_naming(reviewer):
    """
    Test the detection of short variable names in code.
    
    This test verifies that the code review process correctly identifies and flags 
    variables with names that are considered too short (e.g., single-letter variables).
    
    Parameters:
        reviewer (CodeReview): An instance of the CodeReview class used for code analysis.
    
    Raises:
        AssertionError: If no issue is found for the short variable name 'x'.
    
    Example:
        A code snippet with single-letter variables like 'x' and 'y' should trigger 
        a naming convention warning.
    """
    code = """
def bad_names():
    x = 1
    y = 2
    return x + y
    """
    issues = reviewer.analyze_code(code)
    assert any(
        "Variable name 'x' is too short" in issue['message']
        for issue in issues
    )

def test_nested_complexity(reviewer):
    """
    Test the detection of excessive code nesting complexity.
    
    This test verifies that the code review system can identify functions with overly nested conditional statements, which can negatively impact code readability and maintainability.
    
    Parameters:
        reviewer (CodeReview): An instance of the CodeReview class used for analyzing code complexity.
    
    Raises:
        AssertionError: If the code review does not detect and flag excessive nesting.
    
    Example:
        The test uses a sample function with multiple nested if statements to trigger the complexity detection mechanism.
    """
    code = """
def complex_function(a, b, c, d):
    if a:
        if b:
            if c:
                if d:
                    return True
    return False
    """
    issues = reviewer.analyze_code(code)
    assert any(
        "Code is too nested" in issue['message']
        for issue in issues
    )

class TestCodeReviewFeatures:
    def test_comment_generation(self, reviewer):
        """
        Test the generation of review comments for code issues.
        
        This test verifies that review comments are correctly generated with the following characteristics:
        - Include the line number where the issue was found
        - Contain the specific issue description
        - Display the appropriate severity emoji for high-severity issues
        
        Parameters:
            reviewer (CodeReview): An instance of the CodeReview class used for generating review comments
        
        Asserts:
            - The comment contains the line number
            - The comment includes the issue description
            - The comment has the correct severity emoji for high-severity issues
        """
        issue = reviewer.format_suggestion(10, "Test issue", "high")
        comment = reviewer.generate_review_comment(issue)
        assert "Line 10" in comment
        assert "Test issue" in comment
        assert "🔴" in comment  # High severity emoji
    
    def test_suggestion_format(self, reviewer):
        """
        Test the formatting of code suggestions with invalid severity.
        
        This test verifies that:
        - When an invalid severity is provided, the suggestion defaults to "info"
        - The line number is correctly captured in the suggestion
        - The suggestion message contains the expected text
        
        Parameters:
            reviewer (CodeReview): An instance of the CodeReview class used for generating suggestions
        
        Raises:
            AssertionError: If the suggestion formatting does not meet the expected criteria
        """
        suggestion = reviewer.format_suggestion(
            line_number=10,
            message="Consider using a more descriptive variable name",
            severity="warning"  # Invalid severity
        )
        # Should default to "info" for invalid severity
        assert suggestion['severity'] == "info"
        assert suggestion['line'] == 10
        assert "descriptive variable name" in suggestion['message']

    @pytest.mark.parametrize("severity,expected_emoji", [
        ("high", "🔴"),
        ("medium", "🟡"),
        ("low", "🟢"),
        ("info", "ℹ️")
    ])
    def test_severity_emojis(self, reviewer, severity, expected_emoji):
        """
        Test the mapping of severity levels to their corresponding emoji indicators.
        
        Parameters:
            reviewer (CodeReview): An instance of the CodeReview class for generating suggestions and comments
            severity (str): The severity level to test (e.g., 'high', 'medium', 'low', 'info')
            expected_emoji (str): The emoji expected to be associated with the given severity level
        
        Verifies that:
            - A suggestion is correctly formatted with the given severity
            - The generated review comment contains the expected emoji for that severity level
        
        Raises:
            AssertionError: If the expected emoji is not found in the generated comment
        """
        issue = reviewer.format_suggestion(1, "Test message", severity)
        comment = reviewer.generate_review_comment(issue)
        assert expected_emoji in comment 