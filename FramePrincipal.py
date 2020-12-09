"""Subclass of FramePrincipal, which is generated by wxFormBuilder."""
import self as self

import guiperfumes
from FrameMarca import FrameMarca
from FramePerfumes import FramePerfumes
from FrameVolumes import FrameVolumes
from FrameFixacoes import FrameFixacoes
import FrameEssencias


# Implementing FramePrincipal
class FramePrincipal(guiperfumes.FramePrincipal):
    def __init__(self, parent):
        guiperfumes.FramePrincipal.__init__(self, parent)
        self.frameMarca = None
        self.framePerfume = None

    # Handlers for FramePrincipal events.
    def fecharFramePrincipal(self, event):
        self.Destroy()

    def abrirMarca(self, event):

        if not self.frameMarca:
            self.FrameMarca = FrameMarca(self)
        self.FrameMarca.Show(True)

    def abrirFixacoes(self, event):
        if not self.frameMarca:
            self.FrameFixacoes = FrameFixacoes(self)
        self.FrameFixacoes.Show(True)

    def AbrirEssencias(self, event):
        if not self.frameMarca:
            self.FrameEssencias = FrameEssencias.FrameEssencias(self)
        self.FrameEssencias.Show(True)

    def abrirVolumes(self, event):

        if not self.frameMarca:
            self.FrameVolumes = FrameVolumes(self)
        self.FrameVolumes.Show(True)

    def abrirPerfume(self, event):
        if not self.framePerfume:
            self.framePerfume = FramePerfumes(self)
        self.framePerfume.Show(True)


def fecharApp(self, event):
    # TODO: Implement fecharApp

    pass
