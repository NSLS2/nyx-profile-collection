from ophyd import Device, Component as Cpt, EpicsMotor


# Temporary test motor
class TestMotor(Device):
    e = Cpt(EpicsMotor, "-Ax:E}Mtr")
    f = Cpt(EpicsMotor, "-Ax:F}Mtr")
    ctr = Cpt(EpicsMotor, "-Ax:XCtr}Mtr")
    gap = Cpt(EpicsMotor, "-Ax:XGap}Mtr")


class XYMotor(Device):
    x = Cpt(EpicsMotor, "-Ax:X}Mtr")
    y = Cpt(EpicsMotor, "-Ax:Y}Mtr")


class Slits(Device):
    b = Cpt(EpicsMotor, "-Ax:B}Mtr")
    i = Cpt(EpicsMotor, "-Ax:I}Mtr")
    o = Cpt(EpicsMotor, "-Ax:O}Mtr")
    t = Cpt(EpicsMotor, "-Ax:T}Mtr")
    x_ctr = Cpt(EpicsMotor, "-Ax:XCtr}Mtr")
    x_gap = Cpt(EpicsMotor, "-Ax:XGap}Mtr")
    y_ctr = Cpt(EpicsMotor, "-Ax:YCtr}Mtr")
    y_gap = Cpt(EpicsMotor, "-Ax:YGap}Mtr")


class DCM(Device):
    # Virtual Motor
    energy = Cpt(EpicsMotor, "-Ax:E}Mtr")
    c2_bnd = Cpt(EpicsMotor, "-Ax:C2Bnd}Mtr")
    fine_pitch = Cpt(EpicsMotor, "-Ax:FP}Mtr")
    fine_roll = Cpt(EpicsMotor, "-Ax:FR}Mtr")

    # Real Motors
    bragg = Cpt(EpicsMotor, "-Ax:B}Mtr")
    perp = Cpt(EpicsMotor, "-Ax:Perp}Mtr")
    para = Cpt(EpicsMotor, "-Ax:Para}Mtr")
    pitch = Cpt(EpicsMotor, "-Ax:P}Mtr")
    roll = Cpt(EpicsMotor, "-Ax:R}Mtr")
    yaw = Cpt(EpicsMotor, "-Ax:Yaw}Mtr")
    c2_bnd1 = Cpt(EpicsMotor, "-Ax:Bnd1}Mtr")
    c2_bnd2 = Cpt(EpicsMotor, "-Ax:Bnd2}Mtr")
    c1_bnd = Cpt(EpicsMotor, "-Ax:Bnd}Mtr")


class Mirror(Device):
    y = Cpt(EpicsMotor, "-Ax:Y}Mtr")
    x = Cpt(EpicsMotor, "-Ax:X}Mtr")
    p = Cpt(EpicsMotor, "-Ax:P}Mtr")
    r = Cpt(EpicsMotor, "-Ax:R}Mtr")
    bnd1 = Cpt(EpicsMotor, "-Ax:Bnd1}Mtr")
    bnd2 = Cpt(EpicsMotor, "-Ax:Bnd2}Mtr")


# Endstation devices
class SampleCam(Device):
    x = Cpt(EpicsMotor, "-Ax:X}Mtr")
    z = Cpt(EpicsMotor, "-Ax:Z}Mtr")
    focus = Cpt(EpicsMotor, "-Ax:F}Mtr")


class BeamPipe(Device):
    pitch = Cpt(EpicsMotor, "-Ax:P")


class Global(Device):
    x = Cpt(EpicsMotor, "-Ax:X}Mtr")
    yaw = Cpt(EpicsMotor, "-Ax:Yaw}Mtr")


class Goniometer(Device):
    omega = Cpt(EpicsMotor, "-Ax:O}Mtr")
    vert = Cpt(EpicsMotor, "-Ax:V}Mtr")
    x = Cpt(EpicsMotor, "-Ax:X}Mtr")
    y = Cpt(EpicsMotor, "-Ax:Y}Mtr")
    z = Cpt(EpicsMotor, "-Ax:Z}Mtr")
    kappa = Cpt(EpicsMotor, "-Ax:K}Mtr")


class Optic(Device):
    vert = Cpt(EpicsMotor, "-Ax:V}Mtr")


class BeamStop(Device):
    vert = Cpt(EpicsMotor, "-Ax:V}Mtr")
    horiz = Cpt(EpicsMotor, "-Ax:H}Mtr")
    z = Cpt(EpicsMotor, "-Ax:Z}Mtr")


class Table(Device):
    vctr = Cpt(EpicsMotor, "-Ax:VCtr}Mtr")
    vo = Cpt(EpicsMotor, "-Ax:VO}Mtr")
    vi = Cpt(EpicsMotor, "-Ax:VI}Mtr")
    hu = Cpt(EpicsMotor, "-Ax:HU}Mtr")
    hd = Cpt(EpicsMotor, "-Ax:HD}Mtr")


class Detector(Device):
    z = Cpt(EpicsMotor, "-Ax:Z}Mtr")


class Robot(Device):
    lid = Cpt(EpicsMotor, "-Ax:Lid}Mtr")


#######################################################
# NYX
#######################################################

# Test Motor (temporary)
tstmtr = TestMotor("XF:19IDC-OP{Test", name="tstmtr")

# Beam Mask
beam_mask = XYMotor("XF:19IDC-OP{BM:1", name="beam_mask")

# BPMs
bpm1 = XYMotor("XF:19IDC-OP{BPM:1", name="bpm1")
bpm2 = XYMotor("XF:19IDC-OP{BPM:2", name="bpm2")
bpm3 = XYMotor("XF:19IDC-OP{BPM:3", name="bpm3")

# Slits
wb_slits = Slits("XF:19IDC-OP{Slt:WB", name="wb_slits")
mb_slits = Slits("XF:19IDC-OP{Slt:MB", name="mb_slits")

# Mono
dcm = DCM("XF:19IDC-OP{Mono:DCM", name="dcm")

# Mirror
mirror = Mirror("XF:19IDC-OP{Mir:1", name="mirror")

# High Magnification Camera
cam_himag = SampleCam("XF:19IDC-ES{Cam:HiMag", name="cam_himag")

# Low Magnification Camera
cam_lomag = SampleCam("XF:19IDC-ES{Cam:LoMag", name="cam_lomag")

# Beam Pipe
bp = BeamPipe("XF:19IDC-ES{BP:1", name="bp")

# Global Axes
gbl = Global("XF:19IDC-ES{Gbl:1", name="gbl")

# Goniometer
gonio = Goniometer("XF:19IDC-ES{Gon:1", name="gonio")

# Optic
optic = Optic("XF:19IDC-ES{Opt:1", name="optic")

# Beam Stop
bs = BeamStop("XF:19IDC-ES{BS:1", name="bs")

# Beam Definition Slits
bd_slits = Slits("XF:19IDC-ES{Slt:BD", name="bd_slits")

# Detector
det = Detector("XF:19IDC-ES{Det:1", name="det")

# Table
table = Detector("XF:19IDC-ES{Tbl:1", name="table")

# Robot
rbt = Robot("XF:19IDC-ES{Rbt:1", name="rbt")

