import npyscreen


def turbo(set=False, val=0):
    # f = "/sys/devices/system/cpu/intel_pstate/no_turbo"
    f = "no_turbo"
    if set:
        with open(f, "w") as tf:
            tf.write(val)
    with open(f, "r") as tf:
        if tf.read() == "0":
            return False
        return True


def maxperf(set=False, val=0):
    # f = "/sys/devices/system/cpu/intel_pstate/max_perf_pct"
    f = "max_perf_pct"
    if set:
        with open(f, "w") as maxf:
            maxf.write(val)
    with open(f, "r") as maxf:
        return maxf.read()


def minperf(set=False, val=0):
    # f = "/sys/devices/system/cpu/intel_pstate/min_perf_pct"
    f = "min_perf_pct"
    if set:
        with open(f, "w") as minf:
            minf.write(val)
    with open(f, "r") as minf:
        return minf.read()


class FormObject(npyscreen.ActionFormV2):
    def create(self):
        self.show_atx = 30
        self.show_aty = 5
        self.nextrely += 1
        self.mx = self.add(npyscreen.TitleSlider, out_of=100, name="max")
        self.mx.value = float(int(maxperf()))
        self.mn = self.add(npyscreen.TitleSlider, out_of=100, name="min")
        self.mn.value = float(int(minperf()))
        self.tb = self.add(npyscreen.CheckBox, name="Turbo")
        self.tb.value = turbo()

    def afterEditing(self):
        self.parentApp.setNextForm(None)
        pass

    def on_ok(self):
        # pass
        maxperf(True, str('{0:g}'.format(self.mx.value)))
        minperf(True, str('{0:g}'.format(self.mn.value)))

    def on_cancel(self):
        pass
        # self.lname.value = "Cancel button pressed!"


class App(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', FormObject, name='CPUctrl', lines=10, columns=60)


if __name__ == "__main__":
    app = App().run()
    #print(FormObject().mx.value)
