"""This module defines actions (functions) that operate on Labels layers.

The Actions in LABELS_ACTIONS are registered with the application when it is
created in `_app_model._app`.  Modifying this list at runtime will have no
effect.  Use `app.register_action` to register new actions at runtime.
"""

from __future__ import annotations

from app_model.types import Action, ToggleRule

from napari._app_model.actions import (
    AttrRestoreCallback,
    RepeatableAction,
)
from napari._app_model.constants import CommandId
from napari.layers.labels import _labels_key_bindings as _labels_actions

# actions ported to app_model from components/_viewer_key_bindings
LABELS_ACTIONS = [
    Action(
        id=CommandId.LABELS_ACTIVATE_PAINT_MODE,
        title=CommandId.LABELS_ACTIVATE_PAINT_MODE.description,
        short_title=CommandId.LABELS_ACTIVATE_PAINT_MODE.title,
        callback=AttrRestoreCallback(
            _labels_actions.activate_labels_paint_mode, "mode"
        ),
    ),
    Action(
        id=CommandId.LABELS_ACTIVATE_FILL_MODE,
        title=CommandId.LABELS_ACTIVATE_FILL_MODE.description,
        short_title=CommandId.LABELS_ACTIVATE_FILL_MODE.title,
        callback=AttrRestoreCallback(
            _labels_actions.activate_labels_fill_mode, "mode"
        ),
    ),
    Action(
        id=CommandId.LABELS_ACTIVATE_PAN_ZOOM_MODE,
        title=CommandId.LABELS_ACTIVATE_PAN_ZOOM_MODE.description,
        short_title=CommandId.LABELS_ACTIVATE_PAN_ZOOM_MODE.title,
        callback=AttrRestoreCallback(
            _labels_actions.activate_labels_pan_zoom_mode, "mode"
        ),
    ),
    Action(
        id=CommandId.LABELS_ACTIVATE_PICKER_MODE,
        title=CommandId.LABELS_ACTIVATE_PICKER_MODE.description,
        short_title=CommandId.LABELS_ACTIVATE_PICKER_MODE.title,
        callback=AttrRestoreCallback(
            _labels_actions.activate_labels_picker_mode, "mode"
        ),
    ),
    Action(
        id=CommandId.LABELS_ACTIVATE_POLYGON_MODE,
        title=CommandId.LABELS_ACTIVATE_POLYGON_MODE.description,
        short_title=CommandId.LABELS_ACTIVATE_POLYGON_MODE.title,
        callback=AttrRestoreCallback(
            _labels_actions.activate_labels_polygon_mode, "mode"
        ),
    ),
    Action(
        id=CommandId.LABELS_ACTIVATE_ERASE_MODE,
        title=CommandId.LABELS_ACTIVATE_ERASE_MODE.description,
        short_title=CommandId.LABELS_ACTIVATE_ERASE_MODE.title,
        callback=AttrRestoreCallback(
            _labels_actions.activate_labels_erase_mode, "mode"
        ),
    ),
    Action(
        id=CommandId.LABELS_ACTIVATE_TRANSFORM_MODE,
        title=CommandId.LABELS_ACTIVATE_TRANSFORM_MODE.description,
        short_title=CommandId.LABELS_ACTIVATE_TRANSFORM_MODE.title,
        callback=AttrRestoreCallback(
            _labels_actions.activate_labels_transform_mode, "mode"
        ),
    ),
    Action(
        id=CommandId.LABELS_RESET_POLYGON,
        title=CommandId.LABELS_RESET_POLYGON.description,
        short_title=CommandId.LABELS_RESET_POLYGON.title,
        callback=_labels_actions.reset_polygon,
    ),
    Action(
        id=CommandId.LABELS_COMPLETE_POLYGON,
        title=CommandId.LABELS_COMPLETE_POLYGON.description,
        short_title=CommandId.LABELS_COMPLETE_POLYGON.title,
        callback=_labels_actions.complete_polygon,
    ),
    Action(
        id=CommandId.LABELS_NEW_LABEL,
        title=CommandId.LABELS_NEW_LABEL.description,
        short_title=CommandId.LABELS_NEW_LABEL.title,
        callback=_labels_actions.new_label,
    ),
    Action(
        id=CommandId.LABELS_DECREMENT_ID,
        title=CommandId.LABELS_DECREMENT_ID.description,
        short_title=CommandId.LABELS_DECREMENT_ID.title,
        callback=_labels_actions.decrease_label_id,
    ),
    Action(
        id=CommandId.LABELS_INCREMENT_ID,
        title=CommandId.LABELS_INCREMENT_ID.description,
        short_title=CommandId.LABELS_INCREMENT_ID.title,
        callback=_labels_actions.increase_label_id,
    ),
    RepeatableAction(
        id=CommandId.LABELS_DECREASE_BRUSH_SIZE,
        title=CommandId.LABELS_DECREASE_BRUSH_SIZE.title,
        callback=_labels_actions.decrease_brush_size,
    ),
    RepeatableAction(
        id=CommandId.LABELS_INCREASE_BRUSH_SIZE,
        title=CommandId.LABELS_INCREASE_BRUSH_SIZE.title,
        callback=_labels_actions.increase_brush_size,
    ),
    Action(
        id=CommandId.LABELS_SWAP,
        title=CommandId.LABELS_SWAP.description,
        short_title=CommandId.LABELS_SWAP.title,
        callback=_labels_actions.swap_selected_and_background_labels,
    ),
    Action(
        id=CommandId.LABELS_TOGGLE_PRESERVE_LABELS,
        title=CommandId.LABELS_TOGGLE_PRESERVE_LABELS.title,
        callback=_labels_actions.toggle_preserve_labels,
        toggled=ToggleRule(
            get_current=_labels_actions._get_preserve_labels_toggled
        ),
    ),
    Action(
        id=CommandId.LABELS_UNDO,
        title=CommandId.LABELS_UNDO.description,
        short_title=CommandId.LABELS_UNDO.title,
        callback=_labels_actions.undo,
    ),
    Action(
        id=CommandId.LABELS_REDO,
        title=CommandId.LABELS_REDO.description,
        short_title=CommandId.LABELS_REDO.title,
        callback=_labels_actions.redo,
    ),
]
