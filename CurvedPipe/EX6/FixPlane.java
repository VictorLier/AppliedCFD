// Simcenter STAR-CCM+ macro: FixPlane.java
// Written by Simcenter STAR-CCM+ 18.06.007
package macro;

import java.util.*;

import star.common.*;
import star.base.neo.*;
import star.vis.*;

public class FixPlane extends StarMacro {

  public void execute() {
    execute0();
  }

  private void execute0() {

    Simulation simulation_0 = 
      getActiveSimulation();

    Units units_0 = 
      simulation_0.getUnitsManager().getPreferredUnits(Dimensions.Builder().length(1).build());

    Region region_0 = 
      simulation_0.getRegionManager().getRegion("Region");

    FvRepresentation fvRepresentation_0 = 
      ((FvRepresentation) simulation_0.getRepresentationManager().getObject("Volume Mesh"));

    simulation_0.getDataSourceManager().getPartExtents(new NeoObjectVector(new Object[] {region_0}), fvRepresentation_0);

    Scene scene_0 = 
      simulation_0.getSceneManager().getScene("Mesh Scene 1");

    scene_0.setTransparencyOverrideMode(SceneTransparencyOverride.MAKE_SCENE_TRANSPARENT);

    CurrentView currentView_0 = 
      scene_0.getCurrentView();

    currentView_0.setInput(new DoubleVector(new double[] {0.3775331202129135, 0.10976400370304962, 0.061958191512959976}), new DoubleVector(new double[] {2.3638533969455024, -2.9331564486477633, 0.006948691884299592}), new DoubleVector(new double[] {0.20921791279549254, 0.11902435870074886, 0.970598303625931}), 0.8141020484525472, 0, 10.0);

    currentView_0.setInput(new DoubleVector(new double[] {0.4039382357757062, 0.13876350832551765, 0.03946655011049646}), new DoubleVector(new double[] {2.5931231549259808, -3.214933094630294, -0.021161118250801976}), new DoubleVector(new double[] {0.20921791279549254, 0.11902435870074886, 0.970598303625931}), 0.8141020484525472, 0, 10.0);

    currentView_0.setInput(new DoubleVector(new double[] {0.4451760863394063, 0.15170317475550688, 0.014476464251485868}), new DoubleVector(new double[] {2.844388778217446, -3.5237430537170384, -0.05196774982059865}), new DoubleVector(new double[] {0.20921791279549254, 0.11902435870074886, 0.970598303625931}), 0.8141020484525472, 0, 10.0);

    currentView_0.setInput(new DoubleVector(new double[] {0.49401602731277583, 0.16016995582405702, -0.012971629270657675}), new DoubleVector(new double[] {3.119334042400307, -3.8616557163056395, -0.08567764353620874}), new DoubleVector(new double[] {0.20921791279549254, 0.11902435870074886, 0.970598303625931}), 0.8141020484525472, 0, 10.0);

    currentView_0.setInput(new DoubleVector(new double[] {0.5485601086069116, 0.1677083646238149, -0.04302474510115564}), new DoubleVector(new double[] {3.4200617112814147, -4.231255416841281, -0.1225486105101409}), new DoubleVector(new double[] {0.20921791279549254, 0.11902435870074886, 0.970598303625931}), 0.8141020484525472, 0, 10.0);

    currentView_0.setInput(new DoubleVector(new double[] {0.6085521723560219, 0.1754313790763229, -0.0759015563928553}), new DoubleVector(new double[] {3.7489504939797933, -4.635465631508657, -0.1628722943603384}), new DoubleVector(new double[] {0.20921791279549254, 0.11902435870074886, 0.970598303625931}), 0.8141020484525472, 0, 10.0);

    currentView_0.setInput(new DoubleVector(new double[] {0.6742629719097595, 0.18371947794587573, -0.1118587326953251}), new DoubleVector(new double[] {4.108625687078379, -5.077512896909741, -0.20697057176667702}), new DoubleVector(new double[] {0.20921791279549254, 0.11902435870074886, 0.970598303625931}), 0.8141020484525472, 0, 10.0);

    currentView_0.setInput(new DoubleVector(new double[] {0.7461553465757502, 0.1927355038198355, -0.15118227236039283}), new DoubleVector(new double[] {4.50196555017911, -5.5609346457353706, -0.25519633415122067}), new DoubleVector(new double[] {0.20921791279549254, 0.11902435870074886, 0.970598303625931}), 0.8141020484525472, 0, 10.0);

    scene_0.getCreatorGroup().setQuery(null);

    scene_0.getCreatorGroup().setObjects(region_0);

    PlaneSection planeSection_0 = 
      ((PlaneSection) simulation_0.getPartManager().getObject("Plane Section 3"));

    planeSection_0.setBatched(true);

    LabCoordinateSystem labCoordinateSystem_0 = 
      simulation_0.getCoordinateSystemManager().getLabCoordinateSystem();

    planeSection_0.setCoordinateSystem(labCoordinateSystem_0);

    planeSection_0.getInputParts().setQuery(null);

    planeSection_0.getInputParts().setObjects(region_0);

    planeSection_0.getOriginCoordinate().setUnits0(units_0);

    planeSection_0.getOriginCoordinate().setUnits1(units_0);

    planeSection_0.getOriginCoordinate().setUnits2(units_0);

    planeSection_0.getOriginCoordinate().setDefinition("");

    planeSection_0.getOriginCoordinate().setValue(new DoubleVector(new double[] {0.0, 0.0, -0.416}));

    planeSection_0.getOriginCoordinate().setCoordinate(units_0, units_0, units_0, new DoubleVector(new double[] {0.0, 0.0, -0.416}));

    planeSection_0.getOriginCoordinate().setCoordinateSystem(labCoordinateSystem_0);

    planeSection_0.getOrientationCoordinate().setUnits0(units_0);

    planeSection_0.getOrientationCoordinate().setUnits1(units_0);

    planeSection_0.getOrientationCoordinate().setUnits2(units_0);

    planeSection_0.getOrientationCoordinate().setDefinition("");

    planeSection_0.getOrientationCoordinate().setValue(new DoubleVector(new double[] {0.0, 0.0, 1.0}));

    planeSection_0.getOrientationCoordinate().setCoordinate(units_0, units_0, units_0, new DoubleVector(new double[] {0.0, 0.0, 1.0}));

    planeSection_0.getOrientationCoordinate().setCoordinateSystem(labCoordinateSystem_0);

    SingleValue singleValue_0 = 
      planeSection_0.getSingleValue();

    singleValue_0.getValueQuantity().setValue(0.0);

    singleValue_0.getValueQuantity().setUnits(units_0);

    RangeMultiValue rangeMultiValue_0 = 
      planeSection_0.getRangeMultiValue();

    rangeMultiValue_0.setNValues(2);

    rangeMultiValue_0.getStartQuantity().setValue(0.0);

    rangeMultiValue_0.getStartQuantity().setUnits(units_0);

    rangeMultiValue_0.getEndQuantity().setValue(1.0);

    rangeMultiValue_0.getEndQuantity().setUnits(units_0);

    DeltaMultiValue deltaMultiValue_0 = 
      planeSection_0.getDeltaMultiValue();

    deltaMultiValue_0.setNValues(2);

    deltaMultiValue_0.getStartQuantity().setValue(0.0);

    deltaMultiValue_0.getStartQuantity().setUnits(units_0);

    deltaMultiValue_0.getDeltaQuantity().setValue(1.0);

    deltaMultiValue_0.getDeltaQuantity().setUnits(units_0);

    MultiValue multiValue_0 = 
      planeSection_0.getArbitraryMultiValue();

    multiValue_0.getValueQuantities().setUnits(units_0);

    multiValue_0.getValueQuantities().setArray(new DoubleVector(new double[] {0.0}));

    planeSection_0.setValueMode(ValueMode.SINGLE);

    planeSection_0.setBatched(false);

    PartDisplayer partDisplayer_0 = 
      ((PartDisplayer) scene_0.getDisplayerManager().getObject("Section Surface 4"));

    partDisplayer_0.getVisibleParts().addParts();

    partDisplayer_0.getHiddenParts().addParts();

    scene_0.setTransparencyOverrideMode(SceneTransparencyOverride.USE_DISPLAYER_PROPERTY);
  }
}
