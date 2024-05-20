# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.14-5 replay file
# Internal Version: 2015_08_18-20.07.49 135153
# Run by JEEVAN on Wed Jun 22 11:52:52 2022
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=158.338531494141, 
    height=134.273147583008)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
iges = mdb.openIges(
    'C:/Users/JEEVAN/OneDrive/Desktop/meta materials/metamaterial BCC 5mm.igs', 
    msbo=False, trimCurve=DEFAULT, scaleFromFile=OFF)
mdb.models['Model-1'].PartFromGeometryFile(name='metamaterial BCC 5mm', 
    geometryFile=iges, combine=False, stitchTolerance=1.0, 
    dimensionality=THREE_D, type=DEFORMABLE_BODY, convertToAnalytical=1, 
    stitchEdges=1, scale=10.0)
p = mdb.models['Model-1'].parts['metamaterial BCC 5mm']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1894.14, 
    farPlane=3400.26, width=1602.91, height=734.398, cameraPosition=(1555.27, 
    1742.96, 2092.27), cameraTarget=(37.948, 225.639, 574.951))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1801.37, 
    farPlane=3365.31, width=1524.4, height=698.428, cameraPosition=(674.853, 
    -115.019, -1981.53), cameraUpVector=(-0.474519, -0.815452, 0.331465), 
    cameraTarget=(31.5854, 212.212, 545.51))
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['Model-1'].Material(name='ABS')
mdb.models['Model-1'].materials['ABS'].Conductivity(table=((0.15, ), ))
mdb.models['Model-1'].materials['ABS'].Density(table=((1100.0, ), ))
mdb.models['Model-1'].materials['ABS'].SpecificHeat(table=((1.8, ), ))
mdb.models['Model-1'].HomogeneousSolidSection(name='meta material', 
    material='ABS', thickness=None)
p = mdb.models['Model-1'].parts['metamaterial BCC 5mm']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(cells=cells, name='Set-1')
p = mdb.models['Model-1'].parts['metamaterial BCC 5mm']
p.SectionAssignment(region=region, sectionName='meta material', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['metamaterial BCC 5mm']
a.Instance(name='metamaterial BCC 5mm-1', part=p, dependent=ON)
mdb.saveAs(
    pathName='C:/Users/JEEVAN/OneDrive/Desktop/meta materials/meta maaterial BCC 5mm')
#: The model database has been saved to "C:\Users\JEEVAN\OneDrive\Desktop\meta materials\meta maaterial BCC 5mm.cae".
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].HeatTransferStep(name='Step-1', previous='Initial', 
    response=STEADY_STATE, timePeriod=0.05, initialInc=0.05, minInc=5e-07, 
    maxInc=0.05, amplitude=RAMP)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
mdb.models['Model-1'].TabularAmplitude(name='Amp-1', timeSpan=STEP, 
    smooth=SOLVER_DEFAULT, data=((0.0, 0.0), (0.05, 60.0)))
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['metamaterial BCC 5mm-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#0:1498 #10000000 ]', ), )
region = a.Surface(side1Faces=side1Faces1, name='Surf-1')
mdb.models['Model-1'].SurfaceHeatFlux(name='Load-1', createStepName='Step-1', 
    region=region, magnitude=60.0, amplitude='Amp-1')
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['metamaterial BCC 5mm-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#0:1498 #10000000 ]', ), )
region = a.Set(faces=faces1, name='Set-1')
mdb.models['Model-1'].TemperatureBC(name='BC-1', createStepName='Step-1', 
    region=region, fixed=OFF, distributionType=UNIFORM, fieldName='', 
    magnitude=120.0, amplitude=UNSET)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2010.94, 
    farPlane=3286.45, width=1701.75, height=779.685, cameraPosition=(1480.99, 
    -1875.4, 1182.15), cameraUpVector=(0.392527, 0.440472, -0.807407), 
    cameraTarget=(37.9479, 225.639, 541.816))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
mdb.save()
#: The model database has been saved to "C:\Users\JEEVAN\OneDrive\Desktop\meta materials\meta maaterial BCC 5mm.cae".
p = mdb.models['Model-1'].parts['metamaterial BCC 5mm']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
p = mdb.models['Model-1'].parts['metamaterial BCC 5mm']
p.seedPart(size=30.0, deviationFactor=0.1, minSizeFactor=0.1)
elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD, 
    kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF, 
    hourglassControl=DEFAULT, distortionControl=DEFAULT)
elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD, 
    secondOrderAccuracy=OFF, distortionControl=DEFAULT)
p = mdb.models['Model-1'].parts['metamaterial BCC 5mm']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
pickedRegions =(cells, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
    elemType3))
p = mdb.models['Model-1'].parts['metamaterial BCC 5mm']
c = p.cells
pickedRegions = c.getSequenceFromMask(mask=('[#1 ]', ), )
p.setMeshControls(regions=pickedRegions, elemShape=TET, technique=FREE)
elemType1 = mesh.ElemType(elemCode=C3D20R)
elemType2 = mesh.ElemType(elemCode=C3D15)
elemType3 = mesh.ElemType(elemCode=C3D10)
p = mdb.models['Model-1'].parts['metamaterial BCC 5mm']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
pickedRegions =(cells, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
    elemType3))
p = mdb.models['Model-1'].parts['metamaterial BCC 5mm']
p.generateMesh()
