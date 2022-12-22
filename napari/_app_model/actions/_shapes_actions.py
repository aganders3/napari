"""This module defines actions (functions) that operate on Shapes layers.

The Actions in SHAPES_ACTIONS are registered with the application when it is
created in `_app_model._app`.  Modifying this list at runtime will have no
effect.  Use `app.register_action` to register new actions at runtime.
"""

from __future__ import annotations

from app_model.types import Action

from napari._app_model.actions import GeneratorCallback
from napari._app_model.constants import CommandId
from napari.layers.shapes import _shapes_key_bindings as _shapes_actions

# actions ported to app_model from components/_viewer_key_bindings
SHAPES_ACTIONS = [
    Action(
        id=CommandId.SHAPES_HOLD_TO_PAN_ZOOM,
        title=CommandId.SHAPES_HOLD_TO_PAN_ZOOM.description,
        short_title=CommandId.SHAPES_HOLD_TO_PAN_ZOOM.title,
        callback=GeneratorCallback(_shapes_actions.hold_to_pan_zoom),
    ),
    Action(
        id=CommandId.SHAPES_HOLD_TO_LOCK_ASPECT_RATIO,
        title=CommandId.SHAPES_HOLD_TO_LOCK_ASPECT_RATIO.description,
        short_title=CommandId.SHAPES_HOLD_TO_LOCK_ASPECT_RATIO.title,
        callback=GeneratorCallback(_shapes_actions.hold_to_lock_aspect_ratio),
    ),
    # TODO: register_shapes_mode_action (register_layer_attr_action)
    # SHAPES_ACTIVATE_ADD_RECTANGLE_MODE = "napari:shapes:activate_add_rectangle_mode"
    # SHAPES_ACTIVATE_ADD_ELLIPSE_MODE = "napari:shapes:activate_add_ellipse_mode"
    # SHAPES_ACTIVATE_ADD_LINE_MODE = "napari:shapes:activate_add_line_mode"
    # SHAPES_ACTIVATE_ADD_PATH_MODE = "napari:shapes:activate_add_path_mode"
    # SHAPES_ACTIVATE_ADD_POLYGON_MODE = "napari:shapes:activate_add_polygon_mode"
    # SHAPES_ACTIVATE_DIRECT_MODE = "napari:shapes:activate_direct_mode"
    # SHAPES_ACTIVATE_SELECT_MODE = "napari:shapes:activate_select_mode"
    # SHAPES_ACTIVATE_PAN_ZOOM_MODE = "napari:shapes:activate_shape_pan_zoom_mode"
    # SHAPES_ACTIVATE_VERTEX_INSERT_MODE = "napari:shapes:activate_vertex_insert_mode"
    # SHAPES_ACTIVATE_VERTEX_REMOVE_MODE = "napari:shapes:activate_vertex_remove_mode"
    Action(
        id=CommandId.SHAPES_COPY,
        title=CommandId.SHAPES_COPY.description,
        short_title=CommandId.SHAPES_COPY.title,
        callback=_shapes_actions.copy_selected_shapes,
    ),
    Action(
        id=CommandId.SHAPES_PASTE,
        title=CommandId.SHAPES_PASTE.description,
        short_title=CommandId.SHAPES_PASTE.title,
        callback=_shapes_actions.paste_shape,
    ),
    Action(
        id=CommandId.SHAPES_SELECT_ALL,
        title=CommandId.SHAPES_SELECT_ALL.description,
        short_title=CommandId.SHAPES_SELECT_ALL.title,
        callback=_shapes_actions.select_all_shapes,
    ),
    Action(
        id=CommandId.SHAPES_DELETE,
        title=CommandId.SHAPES_DELETE.description,
        short_title=CommandId.SHAPES_DELETE.title,
        callback=_shapes_actions.delete_selected_shapes,
    ),
    Action(
        id=CommandId.SHAPES_MOVE_TO_FRONT,
        title=CommandId.SHAPES_MOVE_TO_FRONT.title,
        callback=_shapes_actions.move_shapes_selection_to_front,
    ),
    Action(
        id=CommandId.SHAPES_MOVE_TO_BACK,
        title=CommandId.SHAPES_MOVE_TO_BACK.title,
        callback=_shapes_actions.move_shapes_selection_to_back,
    ),
    Action(
        id=CommandId.SHAPES_FINISH_DRAWING_SHAPE,
        title=CommandId.SHAPES_FINISH_DRAWING_SHAPE.description,
        short_title=CommandId.SHAPES_FINISH_DRAWING_SHAPE.title,
        callback=_shapes_actions.finish_drawing_shape,
    ),
]
