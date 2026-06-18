from pages.drag_drop_page import DragDropPage


class TestDragDrop:

    def test_drag_drop_perfect(self, driver):
        page = DragDropPage(driver)
        page.open()

        # perform drag and drop and assert Perfect! appears
        page.perform_standard_flow()

        assert page.is_success_visible(), "Expected 'Perfect!' to be visible after drag-and-drop"
