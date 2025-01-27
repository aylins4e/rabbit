import os
import subprocess
import pickle
import yaml
import json
from typing import Any, Dict, List
import base64

# SECURITY: Unsafe deserialization
def load_user_data(data_file: str) -> Dict:
    """Load user data from a pickle file (UNSAFE!)"""
    with open(data_file, 'rb') as f:
        return pickle.load(f)  # Security vulnerability: Unsafe deserialization

# SECURITY: Command injection vulnerability
def run_system_command(user_input: str) -> str:
    """Execute system command (UNSAFE!)"""
    result = os.system(f"echo {user_input}")  # Security vulnerability: Command injection
    return f"Command executed with status: {result}"

# SECURITY: SQL Injection vulnerability
def get_user_by_id(user_id: str) -> str:
    """Get user from database (UNSAFE!)"""
    query = f"SELECT * FROM users WHERE id = {user_id}"  # Security vulnerability: SQL injection
    return f"Executing query: {query}"

# SECURITY: Hardcoded credentials
DB_PASSWORD = "super_secret_password123"  # Security vulnerability: Hardcoded credentials
API_KEY = "sk_live_12345abcdef"

# PERFORMANCE: Memory leak potential
class CacheManager:
    _cache = {}  # Potential memory leak: Unbounded cache growth
    
    def add_to_cache(self, key: str, value: Any):
        self._cache[key] = value  # No cache size limit or cleanup
    
    def get_from_cache(self, key: str) -> Any:
        return self._cache.get(key)

# PERFORMANCE: Inefficient algorithm (O(n^3))
def inefficient_matrix_operation(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix)
    result = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):  # O(n^3) complexity
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix[i][k] * matrix[k][j]
    
    return result

# SECURITY: Unsafe yaml loading
def parse_config(config_file: str) -> Dict:
    """Parse YAML config (UNSAFE!)"""
    with open(config_file, 'r') as f:
        return yaml.load(f)  # Security vulnerability: Unsafe YAML loading

# SECURITY: Weak encryption
def encrypt_data(data: str) -> str:
    """Encrypt data using base64 (VERY WEAK!)"""
    return base64.b64encode(data.encode()).decode()  # Security vulnerability: Weak encryption

# PERFORMANCE: Resource leak
def process_file(filename: str) -> str:
    f = open(filename, 'r')  # Resource leak: File not closed
    content = f.read()
    return content

# SECURITY: Directory traversal
def read_user_file(filename: str) -> str:
    """Read user file (UNSAFE!)"""
    path = f"user_files/{filename}"  # Security vulnerability: Directory traversal
    with open(path) as f:
        return f.read()

# PERFORMANCE: Inefficient string concatenation
def build_large_string(n: int) -> str:
    result = ""
    for i in range(n):
        result += str(i)  # Inefficient string concatenation
    return result

# SECURITY: Unsafe deserialization of JSON
def parse_user_input(user_input: str) -> Dict:
    """Parse user JSON input (UNSAFE!)"""
    return json.loads(user_input)  # Potential security issue: No input validation

# Complex function with multiple security and performance issues
def process_user_request(user_input: Dict) -> Dict:
    """Process user request (UNSAFE!)"""
    # Security vulnerability: No input validation
    username = user_input.get('username', '')
    command = user_input.get('command', '')
    file_path = user_input.get('file_path', '')
    
    # Security vulnerability: Multiple issues in one function
    os.system(f"useradd {username}")  # Command injection
    subprocess.call(f"process {command}", shell=True)  # Shell injection
    
    # Performance issue: Inefficient file handling
    with open(file_path) as f:
        data = f.readlines()
    
    # Security vulnerability: Information exposure
    debug_info = {
        'system_path': os.environ.get('PATH'),
        'secret_key': API_KEY,
        'db_password': DB_PASSWORD
    }
    
    return {
        'status': 'processed',
        'debug': debug_info  # Security vulnerability: Sensitive data exposure
    }

# Configuration with security implications
CONFIG = {
    'debug_mode': True,  # Security issue: Debug mode in production
    'allow_unsafe_uploads': True,  # Security issue: Unsafe file uploads
    'disable_security_checks': True,  # Security issue: Disabled security
    'admin_password': 'admin123',  # Security issue: Weak default password
    'enable_directory_listing': True,  # Security issue: Information disclosure
}

if __name__ == "__main__":
    # Example usage that combines multiple vulnerabilities
    user_data = {
        'username': 'user1; rm -rf /',  # Injection attack
        'command': 'echo "malicious"; cat /etc/passwd',  # Command injection
        'file_path': '../../../etc/passwd'  # Path traversal
    }
    
    # Potential DOS: No request limiting
    while True:  # Performance issue: Infinite loop
        result = process_user_request(user_data)
        cache = CacheManager()
        cache.add_to_cache('result', result)  # Memory leak 