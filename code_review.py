from typing import List, Dict, Optional
import ast
import re

class CodeReview:
    def __init__(self):
        """
        Initialize a new CodeReview instance.
        
        Sets up an empty list to track code review issues and defines valid severity levels for categorizing those issues.
        
        Attributes:
            issues (List[Dict]): A list to store detected code review issues, where each issue is represented as a dictionary.
            severity_levels (Set[str]): A set of predefined severity levels for classifying code review suggestions.
        """
        self.issues: List[Dict] = []
        self.severity_levels = {"high", "medium", "low", "info"}
    
    def analyze_code(self, code_content: str) -> List[Dict]:
        """
        Analyze the provided source code for common programming issues and potential improvements.
        
        This method performs a comprehensive static code analysis by parsing the input code and checking for:
        - Function length exceeding recommended guidelines
        - Inappropriate variable naming conventions
        - Excessive code complexity and nested conditional statements
        
        Parameters:
            code_content (str): The source code to be analyzed, represented as a string.
        
        Returns:
            List[Dict]: A list of detected issues, where each issue is a dictionary containing 
            details such as line number, message, and severity level.
        
        Raises:
            SyntaxError: If the provided code contains invalid Python syntax. In such cases, 
            a high-severity issue is added to the issues list.
        
        Notes:
            - Utilizes Python's Abstract Syntax Tree (AST) for code parsing and analysis
            - Checks are performed using private helper methods
            - Issues are collected in the `self.issues` list
        """
        self.issues = []
        
        # Basic code analysis
        try:
            tree = ast.parse(code_content)
            
            # Check for various code issues
            self._check_function_length(tree)
            self._check_variable_naming(tree)
            self._check_complexity(tree)
            
        except SyntaxError as e:
            self.issues.append(self.format_suggestion(
                e.lineno or 1,
                f"Syntax error in code: {str(e)}",
                "high"
            ))
        
        return self.issues
    
    def _check_function_length(self, tree: ast.AST) -> None:
        """
        Check the length of function definitions in the abstract syntax tree.
        
        This method analyzes each function definition in the provided AST and identifies functions 
        that exceed a predefined length threshold of 20 lines. When a function is found to be 
        excessively long, a suggestion is added to the issues list recommending code refactoring.
        
        Parameters:
            tree (ast.AST): The abstract syntax tree of the code being analyzed.
        
        Side Effects:
            Appends a suggestion to the `issues` list if a function's body exceeds 20 lines.
        
        Severity:
            Generates a "medium" severity suggestion for overly long functions.
        """
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if len(node.body) > 20:  # More than 20 lines
                    self.issues.append(self.format_suggestion(
                        node.lineno,
                        f"Function '{node.name}' is too long ({len(node.body)} lines). Consider breaking it down.",
                        "medium"
                    ))
    
    def _check_variable_naming(self, tree: ast.AST) -> None:
        """
        Check variable naming conventions in the provided abstract syntax tree.
        
        This method analyzes variable names and identifies single-character variables 
        (excluding common loop iterator names 'i', 'j', 'k') that may reduce code readability.
        
        Parameters:
            tree (ast.AST): The abstract syntax tree of the code to analyze.
        
        Side Effects:
            Appends suggestions to the `issues` list for variables with non-descriptive names.
        
        Notes:
            - Skips single-character variables commonly used as loop iterators
            - Suggests using more descriptive variable names
        """
        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                if len(node.id) == 1 and node.id not in ['i', 'j', 'k']:
                    self.issues.append(self.format_suggestion(
                        node.lineno,
                        f"Variable name '{node.id}' is too short. Use more descriptive names.",
                        "low"
                    ))
    
    def _check_complexity(self, tree: ast.AST) -> None:
        """
        Check the complexity of code by analyzing nested if statements.
        
        This method traverses the abstract syntax tree (AST) and identifies if statements to evaluate their nesting depth. 
        It calls the `_check_nested_ifs` method to recursively check the depth of nested conditional statements.
        
        Parameters:
            tree (ast.AST): The abstract syntax tree of the code to be analyzed.
        
        Side Effects:
            Appends complexity-related issues to the `issues` list if nested if statements exceed recommended depth.
        """
        for node in ast.walk(tree):
            if isinstance(node, ast.If):
                self._check_nested_ifs(node, 1)
    
    def _check_nested_ifs(self, node: ast.If, depth: int) -> None:
        """
        Check the depth of nested if statements and append a suggestion if the nesting exceeds recommended complexity.
        
        This method recursively traverses the abstract syntax tree (AST) to analyze the depth of nested if statements. 
        If the nesting depth is greater than 3, it generates a suggestion to restructure the code for improved readability.
        
        Parameters:
            node (ast.If): The current AST node representing an if statement
            depth (int): The current depth of nested if statements
        
        Side Effects:
            - Appends a suggestion to the `issues` list if nesting depth exceeds 3
            - Recursively checks child nodes for further nested if statements
        
        Example:
            # This would trigger a suggestion due to excessive nesting
            if condition1:
                if condition2:
                    if condition3:
                        if condition4:
                            # Deeply nested code
        """
        if depth > 3:
            self.issues.append(self.format_suggestion(
                node.lineno,
                "Code is too nested. Consider restructuring.",
                "medium"
            ))
        for child in ast.iter_child_nodes(node):
            if isinstance(child, ast.If):
                self._check_nested_ifs(child, depth + 1)
    
    def generate_review_comment(self, issue: Dict) -> str:
        """
        Generate a formatted review comment with an emoji indicating the issue's severity.
        
        Parameters:
            issue (Dict): A dictionary containing issue details with keys:
                - 'severity': Severity level of the issue (high, medium, low, info)
                - 'line': Line number where the issue was detected
                - 'message': Descriptive message about the issue
        
        Returns:
            str: A formatted review comment with a severity emoji, line number, and message
        
        Example:
            >>> review = CodeReview()
            >>> issue = {'severity': 'high', 'line': 42, 'message': 'Function too long'}
            >>> review.generate_review_comment(issue)
            '🔴 Line 42: Function too long'
        """
        severity_emoji = {
            "high": "🔴",
            "medium": "🟡",
            "low": "🟢",
            "info": "ℹ️"
        }
        
        return (
            f"{severity_emoji.get(issue['severity'], 'ℹ️')} "
            f"Line {issue['line']}: {issue['message']}"
        )
    
    def format_suggestion(self, line_number: int, message: str, severity: str = "info") -> Dict:
        """
        Format a code suggestion with specified details.
        
        Parameters:
            line_number (int): The line number where the suggestion applies
            message (str): A descriptive message explaining the suggested improvement
            severity (str, optional): The severity level of the suggestion. Defaults to "info".
                Must be a predefined severity level from `self.severity_levels`.
        
        Returns:
            dict: A structured dictionary containing suggestion details with keys:
                - "line": The line number of the suggestion
                - "message": The suggestion description
                - "severity": The severity level (defaults to "info" if invalid)
        
        Example:
            suggestion = self.format_suggestion(10, "Consider breaking down long function", "warning")
        """
        if severity not in self.severity_levels:
            severity = "info"
            
        return {
            "line": line_number,
            "message": message,
            "severity": severity
        } 