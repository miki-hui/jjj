from qgis.core import *
from qgis.gui import *

# save and display the function under custom in expression tab
@qgsfunction(args='auto', group='Custom')
# define the function
def IntersectsLayer(layer_name, feature, parent):
    """ Returns True if a feature is within another layer's feature, else returns False.
    
    <h2>Example usage:</h2>
    <ul>
      <li>IntersectsLayer("layer_name") -> True</li>
      <li>IntersectsLayer("layer_name") -> False</li>
    </ul>
    """
    Intersects = False
    geom = feature.geometry()
    layer = QgsProject.instance().mapLayersByName(layer_name)[0]
    # get features within the geometry
    for feat in layer.getFeatures():
        if geom.within(feat.geometry()):
            Intersects = True
            break
    return Intersects