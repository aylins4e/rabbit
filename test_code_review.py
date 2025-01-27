import pytest
from code_review import CodeReview

@pytest.fixture
def reviewer():
    return CodeReview()

def test_basic_review(reviewer):
    """Test basic code review functionality"""
    code = """
def hello():
    print('world')
    """
    issues = reviewer.analyze_code(code)
    assert isinstance(issues, list)

def test_syntax_error_detection(reviewer):
    """Test detection of syntax errors"""
    code = """
def broken_function()
    print('missing colon')
    """
    issues = reviewer.analyze_code(code)
    assert len(issues) > 0
    assert issues[0]['severity'] == 'high'
    assert 'Syntax error' in issues[0]['message']

def test_long_function_detection(reviewer):
    """Test detection of too long functions"""
    long_function = "def long_func():\n" + "    print('line')\n" * 25
    issues = reviewer.analyze_code(long_function)
    assert any(
        issue['message'].startswith("Function 'long_func' is too long")
        for issue in issues
    )

def test_variable_naming(reviewer):
    """Test variable naming conventions check"""
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
    """Test nested complexity detection"""
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
        """Test if review comments are generated properly"""
        issue = reviewer.format_suggestion(10, "Test issue", "high")
        comment = reviewer.generate_review_comment(issue)
        assert "Line 10" in comment
        assert "Test issue" in comment
        assert "🔴" in comment  # High severity emoji
    
    def test_suggestion_format(self, reviewer):
        """Test if code suggestions are properly formatted"""
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
        """Test different severity levels and their emojis"""
        issue = reviewer.format_suggestion(1, "Test message", severity)
        comment = reviewer.generate_review_comment(issue)
        assert expected_emoji in comment 