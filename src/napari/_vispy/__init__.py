import logging

from qtpy import API_NAME
from vispy import app, use

GL_PLUS = True
try:
    use(gl='gl+')
except RuntimeError:
    GL_PLUS = False
    use(gl='gl2')

# set vispy application to the appropriate qt backend
app.use_app(API_NAME)
del app

# set vispy logger to show warning and errors only
vispy_logger = logging.getLogger('vispy')
vispy_logger.setLevel(logging.WARNING)


from napari._vispy.camera import VispyCamera
from napari._vispy.canvas import VispyCanvas
from napari._vispy.overlays.axes import VispyAxesOverlay
from napari._vispy.overlays.interaction_box import (
    VispySelectionBoxOverlay,
    VispyTransformBoxOverlay,
)
from napari._vispy.overlays.labels_polygon import VispyLabelsPolygonOverlay
from napari._vispy.overlays.scale_bar import VispyScaleBarOverlay
from napari._vispy.overlays.text import VispyTextOverlay
from napari._vispy.utils.visual import create_vispy_layer, create_vispy_overlay

__all__ = [
    'GL_PLUS',
    'VispyAxesOverlay',
    'VispyCamera',
    'VispyCanvas',
    'VispyLabelsPolygonOverlay',
    'VispyScaleBarOverlay',
    'VispySelectionBoxOverlay',
    'VispyTextOverlay',
    'VispyTransformBoxOverlay',
    'create_vispy_layer',
    'create_vispy_overlay',
]
