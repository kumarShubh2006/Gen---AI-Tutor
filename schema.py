from pydantic import BaseModel, Field   
# //BaseModel and Field are classes from the Pydantic library that are used to define data models and their fields with validation and serialization capabilities.

#Input Structure for text
class TextRequest(BaseModel):
    topic: str = Field(..., description="The topic for which the text is requested.",example = "Neural Networks")
    course: str = Field(..., description="The subject for which the text is requested.",example = "Artificial Intelligence")
    student_level: str = Field(..., description="The level of the student for which the text is requested.",example = "Beginner")
    # //This line defines a field named topic of type str. The Field function is used to provide additional metadata, 
    # such as a description for the field such as maximum length or validation rules. ... represents spreading operator which is used to indicate that the field is required and must be provided when creating an instance of the TextRequest model.


