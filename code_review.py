from typing import List, Dict, Optional
import ast
import re

class CodeReview:
    def __init__(self):
        self.issues: List[Dict] = []
        self.severity_levels = {"high", "medium", "low", "info"}
    
    def analyze_code(self, code_content: str) -> List[Dict]:
        """
        Analyze provided code content for common issues
        Args:
            code_content (str): Source code to analyze
        Returns:
            list: List of found issues
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
        """Check if functions are too long"""
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if len(node.body) > 20:  # More than 20 lines
                    self.issues.append(self.format_suggestion(
                        node.lineno,
                        f"Function '{node.name}' is too long ({len(node.body)} lines). Consider breaking it down.",
                        "medium"
                    ))
    
    def _check_variable_naming(self, tree: ast.AST) -> None:
        """Check variable naming conventions"""
        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                if len(node.id) == 1 and node.id not in ['i', 'j', 'k']:
                    self.issues.append(self.format_suggestion(
                        node.lineno,
                        f"Variable name '{node.id}' is too short. Use more descriptive names.",
                        "low"
                    ))
    
    def _check_complexity(self, tree: ast.AST) -> None:
        """Check code complexity"""
        for node in ast.walk(tree):
            if isinstance(node, ast.If):
                self._check_nested_ifs(node, 1)
    
    def _check_nested_ifs(self, node: ast.If, depth: int) -> None:
        """Check for deeply nested if statements"""
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
        Generate a review comment for an issue
        Args:
            issue (dict): Issue details
        Returns:
            str: Formatted review comment
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
        Format a code suggestion
        Args:
            line_number (int): Line number for the suggestion
            message (str): Suggestion message
            severity (str): Suggestion severity level
        Returns:
            dict: Formatted suggestion
        """
        if severity not in self.severity_levels:
            severity = "info"
            
        return {
            "line": line_number,
            "message": message,
            "severity": severity
        } 