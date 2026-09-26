from pydantic import BaseModel, Field, ConfigDict


class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка заданий для определенного курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    course_id: str = Field(alias='courseId')


class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание задания.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias='courseId')
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str = Field(alias='estimatedTime')


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление задания.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None = None
    max_score: int | None = Field(default=None, alias='maxScore')
    min_score: int | None = Field(default=None, alias='minScore')
    order_index: int | None = Field(default=None, alias='orderIndex')
    description: str | None = None
    estimated_time: str | None = Field(default=None, alias='estimatedTime')


class ExerciseSchema(BaseModel):
    """
    Описание структуры задания.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias='courseId')
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str = Field(default=None, alias='estimatedTime')


class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа получения списка заданий.
    """
    exercises: list[ExerciseSchema]


class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания задания.
    """
    exercise: ExerciseSchema