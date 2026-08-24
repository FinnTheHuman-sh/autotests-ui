from components.base_component import BaseComponent, expect
from elements.button import Button
from elements.input import Input
from elements.text import Text


class CreateCourseExerciseFormComponent(BaseComponent):
    def click_delete_button(self, index: int):
        delete_button = Button(self.page, f"create-course-exercise-{index}-box-toolbar-delete-exercise-button",
                               'Delete button')
        delete_button.click()

    def check_visible(self, index: int, title: str, description: str):
        subtitle = Text(self.page, f"create-course-exercise-{index}-box-toolbar-subtitle-text", 'Subtitle')
        title_input = Input(self.page, f"create-course-exercise-form-title-{index}-input", 'Title input')
        description_input = Input(self.page, f"create-course-exercise-form-description-{index}-input", 'Description input')

        subtitle.check_visible()
        subtitle.check_have_text(f"#{index + 1} Exercise")

        title_input.check_visible()
        title_input.check_have_value(title)

        description_input.check_visible()
        description_input.check_have_value(description)

    def fill(self, index: int, title: str, description: str):
        title_input = Input(self.page, f"create-course-exercise-form-title-{index}-input", 'Title input')
        description_input = Input(self.page, f"create-course-exercise-form-description-{index}-input", 'Description input')

        title_input.fill(title)
        title_input.check_have_value(title)

        description_input.fill(description)
        description_input.check_have_value(description)
