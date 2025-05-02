import bluesky.preprocessors as bpp
import bluesky.plans as bp
import bluesky.plan_stubs as bps
import epics


def simple_ascan(camera, stats, motor, start, end, steps):
    """ Simple absolute scan of a single motor against a single camera.

    Automatically plots the results.
    """

    stats_name = "_".join((camera.name,stats)) if stats else camera.name
    try:
        motor_name = motor.readback.name
    except AttributeError:
        try:
            motor_name = motor.gap.name
        except AttributeError:
            motor_name = motor.name

    # Setup plots
    fig, ax1 = plt.subplots()
    ax1.grid(True)

    # Best-Effort Callback table will interfere with LiveTable
    # Check if set, if yes store current setting, disable for scan, reset at end
    try:
        bec
    except NameError:
        bec_exists = False
    else:
        bec_exists = True
        bec_table_enabled = bec._table_enabled
        bec.disable_table()

    @bpp.subs_decorator(LivePlot(stats_name, motor_name, ax=ax1))
    @bpp.subs_decorator(LiveTable([motor_name, stats_name]))
    @bpp.reset_positions_decorator([motor])
    def inner():
        yield from bp.scan([camera], motor, start, end, steps)

    yield from inner()

    # Reset Best-Effort Callback table settings to previous settings
    if bec_exists and bec_table_enabled:
        bec.enable_table()

from bluesky.plan_stubs import null

def hello_world_plan():
    print("Hello, world!")
    yield from null()
