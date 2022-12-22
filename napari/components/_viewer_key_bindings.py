from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from napari.viewer import Viewer

from napari.components.viewer_model import ViewerModel
from napari.settings import get_settings
from napari.utils.action_manager import action_manager
from napari.utils.theme import available_themes


def register_viewer_action(description):
    """
    Convenient decorator to register an action with the current ViewerModel

    It will use the function name as the action name. We force the description
    to be given instead of function docstring for translation purpose.
    """

    def _inner(func):
        action_manager.register_action(
            name=f'napari:{func.__name__}',
            command=func,
            description=description,
            keymapprovider=ViewerModel,
        )
        return func

    return _inner


def reset_scroll_progress(viewer: Viewer):
    # on key press
    viewer.dims._scroll_progress = 0
    yield
    # on key release
    viewer.dims._scroll_progress = 0


def cycle_theme(viewer: Viewer):
    """Toggle theme for viewer"""
    settings = get_settings()
    themes = available_themes()
    current_theme = settings.appearance.theme
    idx = (themes.index(current_theme) + 1) % len(themes)
    settings.appearance.theme = themes[idx]


def reset_view(viewer: Viewer):
    viewer.reset_view()


def increment_dims_left(viewer: Viewer):
    viewer.dims._increment_dims_left()


def increment_dims_right(viewer: Viewer):
    viewer.dims._increment_dims_right()


def focus_axes_up(viewer: Viewer):
    viewer.dims._focus_up()


def focus_axes_down(viewer: Viewer):
    viewer.dims._focus_down()


def roll_axes(viewer: Viewer):
    viewer.dims._roll()


def transpose_axes(viewer: Viewer):
    viewer.dims.transpose()


def toggle_selected_layer_visibility(viewer: Viewer):
    viewer.layers.toggle_selected_visibility()


def toggle_console_visibility(viewer: Viewer):
    viewer.window._qt_viewer.toggle_console_visibility()
