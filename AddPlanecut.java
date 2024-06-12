// Simcenter STAR-CCM+ macro: AddPlanecut.java
// Written by Simcenter STAR-CCM+ 18.06.007
package macro;

import java.util.*;

import star.common.*;
import star.base.neo.*;
import star.vis.*;

public class AddPlanecut extends StarMacro {

  public void execute() {
    execute0();
  }

  private void execute0() {

    Simulation simulation_0 = 
      getActiveSimulation();

    Units units_1 = 
      simulation_0.getUnitsManager().getPreferredUnits(Dimensions.Builder().length(1).build());

    Scene scene_1 = 
      simulation_0.getSceneManager().getScene("Mesh Scene 1");

    scene_1.setTransparencyOverrideMode(SceneTransparencyOverride.MAKE_SCENE_TRANSPARENT);

    scene_1.getCreatorGroup().setQuery(null);

    Region region_0 = 
      simulation_0.getRegionManager().getRegion("Region");

    scene_1.getCreatorGroup().setObjects(region_0);

    scene_1.getCreatorGroup().setQuery(null);

    scene_1.getCreatorGroup().setObjects(region_0);

    PartDisplayer partDisplayer_1 = 
      scene_1.getDisplayerManager().createPartDisplayer("Section Surface", -1, 1);

    scene_1.setTransparencyOverrideMode(SceneTransparencyOverride.MAKE_SCENE_TRANSPARENT);

    PlaneSection planeSection_1 = 
      (PlaneSection) simulation_0.getPartManager().createImplicitPart(new NeoObjectVector(new Object[] {}), new DoubleVector(new double[] {0.0, 0.0, 1.0}), new DoubleVector(new double[] {0.0, 0.0, 0.0}), 0, 1, new DoubleVector(new double[] {0.0}), null);

    LabCoordinateSystem labCoordinateSystem_0 = 
      simulation_0.getCoordinateSystemManager().getLabCoordinateSystem();

    planeSection_1.setCoordinateSystem(labCoordinateSystem_0);

    planeSection_1.getInputParts().setQuery(null);

    planeSection_1.getInputParts().setObjects(region_0);

    planeSection_1.getOriginCoordinate().setUnits0(units_1);

    planeSection_1.getOriginCoordinate().setUnits1(units_1);

    planeSection_1.getOriginCoordinate().setUnits2(units_1);

    planeSection_1.getOriginCoordinate().setDefinition("");

    planeSection_1.getOriginCoordinate().setValue(new DoubleVector(new double[] {0.0, 0.0, 0.0}));

    planeSection_1.getOriginCoordinate().setCoordinate(units_1, units_1, units_1, new DoubleVector(new double[] {0.0, 0.0, 0.0}));

    planeSection_1.getOriginCoordinate().setCoordinateSystem(labCoordinateSystem_0);

    planeSection_1.getOrientationCoordinate().setUnits0(units_1);

    planeSection_1.getOrientationCoordinate().setUnits1(units_1);

    planeSection_1.getOrientationCoordinate().setUnits2(units_1);

    planeSection_1.getOrientationCoordinate().setDefinition("");

    planeSection_1.getOrientationCoordinate().setValue(new DoubleVector(new double[] {0.0, 1.0, 0.0}));

    planeSection_1.getOrientationCoordinate().setCoordinate(units_1, units_1, units_1, new DoubleVector(new double[] {0.0, 1.0, 0.0}));

    planeSection_1.getOrientationCoordinate().setCoordinateSystem(labCoordinateSystem_0);

    SingleValue singleValue_1 = 
      planeSection_1.getSingleValue();

    singleValue_1.getValueQuantity().setValue(0.0);

    singleValue_1.getValueQuantity().setUnits(units_1);

    RangeMultiValue rangeMultiValue_1 = 
      planeSection_1.getRangeMultiValue();

    rangeMultiValue_1.setNValues(2);

    rangeMultiValue_1.getStartQuantity().setValue(0.0);

    rangeMultiValue_1.getStartQuantity().setUnits(units_1);

    rangeMultiValue_1.getEndQuantity().setValue(1.0);

    rangeMultiValue_1.getEndQuantity().setUnits(units_1);

    DeltaMultiValue deltaMultiValue_1 = 
      planeSection_1.getDeltaMultiValue();

    deltaMultiValue_1.setNValues(2);

    deltaMultiValue_1.getStartQuantity().setValue(0.0);

    deltaMultiValue_1.getStartQuantity().setUnits(units_1);

    deltaMultiValue_1.getDeltaQuantity().setValue(1.0);

    deltaMultiValue_1.getDeltaQuantity().setUnits(units_1);

    MultiValue multiValue_1 = 
      planeSection_1.getArbitraryMultiValue();

    multiValue_1.getValueQuantities().setUnits(units_1);

    multiValue_1.getValueQuantities().setArray(new DoubleVector(new double[] {0.0}));

    planeSection_1.setValueMode(ValueMode.SINGLE);

    partDisplayer_1.getVisibleParts().addParts(planeSection_1);

    partDisplayer_1.getHiddenParts().addParts();

    scene_1.setTransparencyOverrideMode(SceneTransparencyOverride.USE_DISPLAYER_PROPERTY);

    Scene scene_3 = 
      simulation_0.getSceneManager().getScene("Scalar Scene 1");

    scene_3.initializeAndWait();

    Scene scene_4 = 
      simulation_0.getSceneManager().getScene("Scalar Scene 2");

    scene_4.initializeAndWait();

    simulation_0.getSceneManager().createVectorScene("Vector Scene", "Outline", "Vector", null);

    Scene scene_5 = 
      simulation_0.getSceneManager().getScene("Vector Scene 2");

    scene_5.initializeAndWait();

    VectorDisplayer vectorDisplayer_1 = 
      ((VectorDisplayer) scene_5.getDisplayerManager().getObject("Vector 1"));

    Legend legend_1 = 
      vectorDisplayer_1.getLegend();

    PredefinedLookupTable predefinedLookupTable_0 = 
      ((PredefinedLookupTable) simulation_0.get(LookupTableManager.class).getObject("blue-yellow-red"));

    legend_1.setLookupTable(predefinedLookupTable_0);

    SceneUpdate sceneUpdate_3 = 
      scene_5.getSceneUpdate();

    HardcopyProperties hardcopyProperties_5 = 
      sceneUpdate_3.getHardcopyProperties();

    hardcopyProperties_5.setCurrentResolutionWidth(25);

    hardcopyProperties_5.setCurrentResolutionHeight(25);

    SceneUpdate sceneUpdate_1 = 
      scene_1.getSceneUpdate();

    HardcopyProperties hardcopyProperties_3 = 
      sceneUpdate_1.getHardcopyProperties();

    hardcopyProperties_3.setCurrentResolutionWidth(1556);

    hardcopyProperties_3.setCurrentResolutionHeight(833);

    hardcopyProperties_5.setCurrentResolutionWidth(1554);

    hardcopyProperties_5.setCurrentResolutionHeight(832);

    scene_5.resetCamera();

    vectorDisplayer_1.getInputParts().setQuery(null);

    vectorDisplayer_1.getInputParts().setObjects(planeSection_1);

    vectorDisplayer_1.setDisplayMode(VectorDisplayMode.VECTOR_DISPLAY_MODE_LIC);

    vectorDisplayer_1.setDisplayMode(VectorDisplayMode.VECTOR_DISPLAY_MODE_GLYPH);

    vectorDisplayer_1.setDisplayMode(VectorDisplayMode.VECTOR_DISPLAY_MODE_LIC);
  }
}
