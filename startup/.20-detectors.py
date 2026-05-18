from ophyd import (
    AreaDetector,
    SingleTrigger,
    StatsPlugin,
    ROIPlugin,
    TransformPlugin,
    EpicsSignalRO,
)


class StandardCam(SingleTrigger, AreaDetector):
    # Transform
    trans1 = Cpt(TransformPlugin, 'Trans1:')
    
    # Statistics
    stats1 = Cpt(StatsPlugin, "Stats1:")
    stats2 = Cpt(StatsPlugin, "Stats2:")
    stats3 = Cpt(StatsPlugin, "Stats3:")
    stats4 = Cpt(StatsPlugin, "Stats4:")
    stats5 = Cpt(StatsPlugin, "Stats5:")

    # Region of Interest
    roi1 = Cpt(ROIPlugin, "ROI1:")
    roi2 = Cpt(ROIPlugin, "ROI2:")
    roi3 = Cpt(ROIPlugin, "ROI3:")
    roi4 = Cpt(ROIPlugin, "ROI4:")


# CVD screen in the white beam, us of the DCM
cam_wb = StandardCam("XF:19ID-BI{Cam:1}", name="cam_wb")

# Surface of the first DCM crystal
cam_dcm_crystal = StandardCam("XF:19ID-BI{Cam:4}", name="cam_dcm_crystal")

# YAG screen in the monochromatic beam just ds of the DCM
cam_mb = StandardCam("XF:19ID-BI{Cam:2}", name="cam_mb")

# YAG screen just ds of the vertically focusing mirror
cam_mirror = StandardCam("XF:19ID-BI{Cam:3}", name="cam_mirror")

# In-line sample view microscope
cam_sample_inline = StandardCam("XF:19ID-BI{Cam:5}", name="cam_sample_inline")

# Viewing the sample from below
cam_sample_below = StandardCam("XF:19ID-BI{Cam:6}", name="cam_sample_below")

all_cams = [
    cam_wb,
    cam_dcm_crystal,
    cam_mb,
    cam_mirror,
    cam_sample_inline,
    cam_sample_below,
]

for cam in all_cams:
    cam.read_attrs = [f"stats{n}" for n in range(1, 6)]
    for n in range(1, 6):
        getattr(cam, f"stats{n}").read_attrs = [
            "total",
            "min_value",
            "max_value",
            "net",
            "sigma",
            "sigma_x",
            "sigma_y",
            "sigma_xy",
            "centroid",
        ]

# Ion Chambers
ion1 = EpicsSignalRO("XF:19IDD-CT{Ion:1-Gauge:1}Volts-I", name="ion1")
ion2 = EpicsSignalRO("XF:19IDD-CT{Ion:2-Gauge:1}Volts-I", name="ion2")

# PIN-diode
pin_diode = EpicsSignalRO("XF:19ID1-BI:NYX{Keith:1}readFloat", name="pin_diode")
