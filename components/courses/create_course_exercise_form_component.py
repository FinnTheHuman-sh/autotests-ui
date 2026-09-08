import allure  # Импортируем allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.input import Input
from elements.text import Text


class CreateCourseExerciseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.delete_exercise_button = Button(
            page, 'create-course-exercise-{index}-box-toolbar-delete-exercise-button', 'Delete exercise'
        )
        self.subtitle = Text(page, 'create-course-exercise-{index}-box-toolbar-subtitle-text', 'Exercise subtitle')
        self.title_input = Input(page, 'create-course-exercise-form-title-{index}-input', 'Title')
        self.description_input = Input(page, 'create-course-exercise-form-description-{index}-input', 'Description')

    @allure.step('Check visible create course exercise form at index "{index}"')  # Добавили allure шаг
    def check_visible(self, index: int, title: str, description: str):
        self.subtitle.check_visible()
        self.subtitle.check_have_text(f"#{index + 1} Exercise")

        self.title_input.check_visible()
        self.title_input.check_have_value(title)

        self.description_input.check_visible()
        self.description_input.check_have_value(description)

    @allure.step('Fill create course exercise form at index "{index}"')  # Добавили allure шаг
    def fill(self, index: int, title: str, description: str):
        self.title_input.fill(title)
        self.title_input.check_have_value(title)

        self.description_input.fill(description)
        self.description_input.check_have_value(description)

    def click_delete_button(self, index: int):
        self.delete_exercise_button.click()