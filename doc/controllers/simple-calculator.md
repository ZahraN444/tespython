# Simple Calculator

```python
simple_calculator_controller = client.simple_calculator
```

## Class Name

`SimpleCalculatorController`


# Get Calculate

Calculates the expression using the specified operation.

```python
def get_calculate(self,
                 options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | [`OperationType`](../../doc/models/operation-type.md) | Template, Required | The operator to apply on the variables |
| `x` | `float` | Query, Required | The LHS value |
| `y` | `float` | Query, Required | The RHS value |

## Response Type

`float`

## Example Usage

```python
collect = {
    'operation': OperationType.MULTIPLY,
    'x': 222.14,
    'y': 165.14
}
result = simple_calculator_controller.get_calculate(collect)
print(result)
```

