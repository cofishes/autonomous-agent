# 数据结构定义

from typing import Any, List, Dict

class SpatialEvent:
    """
    表示空间事件.
    """
    def __init__(self, position: List[float], timestamp: float) -> None:
        self.position = position  # 位置: [x, y, z]
        self.timestamp = timestamp  # 时间戳

class RigidBody:
    """
    表示刚体.
    """
    def __init__(self, mass: float, velocity: List[float]) -> None:
        self.mass = mass  # 质量
        self.velocity = velocity  # 速度: [vx, vy, vz]

class Decision:
    """
    表示决策.
    """
    def __init__(self, choice: str, confidence: float) -> None:
        self.choice = choice  # 选择
        self.confidence = confidence  # 置信度

class Motion:
    """
    表示运动.
    """
    def __init__(self, position: List[float], orientation: List[float]) -> None:
        self.position = position  # 位置
        self.orientation = orientation  # 定向

class ThinkingRecord:
    """
    表示思考记录.
    """
    def __init__(self, events: List[Dict[str, Any]]) -> None:
        self.events = events  # 事件记录

class Rule:
    """
    表示规则.
    """
    def __init__(self, condition: str, action: str) -> None:
        self.condition = condition  # 条件
        self.action = action  # 动作
