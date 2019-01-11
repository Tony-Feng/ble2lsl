#try to plot data streamed, but not working, and no error

import ble2lsl
from ble2lsl.devices import muse2016
from wizardhat import acquire, plot
import replay

if __name__ == '__main__':
    rep = Replay(muse2016, "\\data")
    receiver = acquire.Receiver()
    plot.Lines(receiver.buffers["EEG"])
