import sqlalchemy as sa
from ...config.database import Base
from datetime import time


class Task(Base):
    __tablename__ = 'taks'

    task_id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    task_status: bool = sa.Column(sa.Boolean, nullable=False)
    sheet_id: int = sa.Column(sa.ForeignKey("sheets.sheet_id"))
    task_type: str = sa.column(sa.String, nullable=False)
    main_column: str = sa.column(sa.String, nullable=False)
    auxiliary_column: str = sa.column(sa.String, nullable=False)
    reference_values: str = sa.column(sa.String, nullable=False)


class TaskRuntime(Base):
    __tablename__ = 'tasks_runtime'

    tasks_runtime_id: int = sa.Column(
        sa.Integer, primary_key=True, autoincrement=True)
    runtime: time = sa.Column(sa.Time, nullable=False)
    task_id: int = sa.Column(sa.ForeignKey("tasks.task_id"))


class AchievedTask(Base):
    __tablename__ = 'achieved_tasks'

    achievied_tasks_id: int = sa.Column(
        sa.Integer, primary_key=True, autoincrement=True)
    task_id: int = sa.Column(sa.ForeignKey("tasks.task_id"))
    date_created = sa.Column(sa.TIMESTAMP(
        timezone=True), server_default=sa.sql.func.now())


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
    task_id: int = sa.Column(sa.ForeignKey("tasks.task_id"))
