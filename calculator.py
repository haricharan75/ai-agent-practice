import math
import ast
import operator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def square_root(a):
    if a < 0:
        return "Error: Cannot calculate square root of a negative number!"
    return math.sqrt(a)

ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

def _safe_eval_node(node):
    if isinstance(node, ast.Expression):
        return _safe_eval_node(node.body)
    elif isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError(f"Unsupported constant type: {type(node.value)}")
    elif isinstance(node, ast.BinOp):
        op_type = type(node.op)
        if op_type not in ALLOWED_OPERATORS:
            raise ValueError(f"Unsupported operator: {op_type.__name__}")
        left = _safe_eval_node(node.left)
        right = _safe_eval_node(node.right)
        if op_type == ast.Div and right == 0:
            raise ValueError("Error: Cannot divide by zero!")
        return ALLOWED_OPERATORS[op_type](left, right)
    elif isinstance(node, ast.UnaryOp):
        op_type = type(node.op)
        if op_type not in ALLOWED_OPERATORS:
            raise ValueError(f"Unsupported unary operator: {op_type.__name__}")
        operand = _safe_eval_node(node.operand)
        return ALLOWED_OPERATORS[op_type](operand)
    else:
        raise ValueError(f"Unsupported expression node: {type(node).__name__}")

def advanced_calculate(expression):
    if not isinstance(expression, str):
        return "Error: Expression must be a string!"
    if len(expression) > 200:
        return "Error: Expression is too long!"
    try:
        tree = ast.parse(expression.strip(), mode='eval')
        result = _safe_eval_node(tree)
        return result
    except ValueError as e:
        return f"Error: {e}"
    except SyntaxError:
        return "Error: Invalid mathematical expression!"
    except Exception:
        return "Error: Could not evaluate expression!"

print("Addition (10 + 5):", add(10, 5))
print("Subtraction (10 - 5):", subtract(10, 5))
print("Multiplication (10 * 5):", multiply(10, 5))
print("Division (10 / 2):", divide(10, 2))
print("Square Root of 25:", square_root(25))
print("Advanced (10 + 5 * 2):", advanced_calculate("10 + 5 * 2"))
