from dataclasses import dataclass
from datetime import time
import sqlalchemy as sa
from ..config.database import Base


@dataclass
class Task(Base):
    __tablename__ = 'tasks'

    task_id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    task_status: bool = sa.Column(sa.Boolean, nullable=False, index=True)
    sheet_name: str = sa.Column(sa.String, nullable=False)
    task_type: str = sa.Column(sa.String, nullable=False)
    main_column: str = sa.Column(sa.String, nullable=False)
    auxiliary_column: str = sa.Column(sa.String, nullable=True)
    reference_values: str = sa.Column(sa.String, nullable=True)


@dataclass
class UserTask(Base):
    __tablename__ = 'users_tasks'

    user_id: int = sa.Column(sa.ForeignKey(
        "users.user_id", ondelete="CASCADE"), primary_key=True)
    task_id: int = sa.Column(sa.ForeignKey(
        "tasks.task_id", ondelete="CASCADE"), primary_key=True)


@dataclass
class TaskRuntime(Base):
    __tablename__ = 'tasks_runtime'

    tasks_runtime_id: int = sa.Column(
        sa.Integer, primary_key=True, autoincrement=True)
    runtime: time = sa.Column(sa.Time, nullable=False, index=True)
    task_id: int = sa.Column(sa.ForeignKey(
        "tasks.task_id", ondelete="CASCADE"), nullable=False)


@dataclass
class AchievedTask(Base):
    __tablename__ = 'achieved_tasks'

    achieved_tasks_id: int = sa.Column(
        sa.Integer, primary_key=True, autoincrement=True)
    created_at = sa.Column(sa.Date, default=sa.func.now(), nullable=False)
    tasks_runtime_id: int = sa.Column(sa.ForeignKey(
        "tasks_runtime.tasks_runtime_id", ondelete="CASCADE"), nullable=False)


@dataclass
class TaskWeekday(Base):
    __tablename__ = 'tasksweekdays'

    task_weekday_id: int = sa.Column(
        sa.Integer, primary_key=True, autoincrement=True)
    sunday: bool = sa.Column(sa.Boolean)
    monday: bool = sa.Column(sa.Boolean)
    tuesday: bool = sa.Column(sa.Boolean)
    wednesday: bool = sa.Column(sa.Boolean)
    thursday: bool = sa.Column(sa.Boolean)
    friday: bool = sa.Column(sa.Boolean)
    saturday: bool = sa.Column(sa.Boolean)
    task_id: int = sa.Column(sa.ForeignKey(
        "tasks.task_id", ondelete="CASCADE"), nullable=False)
