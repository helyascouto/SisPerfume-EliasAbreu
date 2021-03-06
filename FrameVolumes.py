"""Subclass of FrameVolumes, which is generated by wxFormBuilder."""

import wx
import guiperfumes
import db


# Implementing FrameVolumes
class FrameVolumes(guiperfumes.FrameVolumes):
    def __init__(self, parent):
        guiperfumes.FrameVolumes.__init__(self, parent)
        self.atualizarGridVolume()


        # Handlers for FrameEssencias events.

    def adicionarVolume(self, event):
        nome = self.txtNome.GetValue()  # Recupera o conteúdo da caixa de texto
        db.inserirVolume(nome)  # Chama a função inserir Volumes do arquivo db.py
        # Exibe uma mensagem ao usuário confirmado o sucesso na inserção
        wx.MessageBox(message="Volume Inserida com Sucesso", caption="SisPerfumes", style=wx.OK, parent=self)
        self.atualizarGridVolume()  # Atualiza o grid com a relação de Volumes

    def atualizarVolume(self, event):
        nome_Volume = self.gridVolumes.GetCellValue(event.GetRow(),
                                                   event.GetCol())  # Recupera o nome da Volumes editado

        if (nome_Volume):  # Se o conteúdo não for vazio, faça
            id_Volume = int(self.gridVolumes.GetCellValue(event.GetRow(),
                                                         0))  # Pegue na linha editada, o conteúdo da primeira coluna
        db.atualizarVolume(id_Volume, nome_Volume)  # Chame a função para atualizar uma Volumes
        wx.MessageBox(message="Volume Atualizada com Sucesso", caption="SysPerfumes", style=wx.OK,
                      parent=self)

    def atualizarGridVolume(self):
        if (self.gridVolumes.GetNumberRows() > 0):
            self.gridVolumes.DeleteRows(0, self.gridVolumes.GetNumberRows())  # Limpa a tabela

        volume = db.listarVolume()  # Chama a função listar marcas, retornando a lista de marcas existentes

        for volume in volume:
            self.gridVolumes.AppendRows(1)  # Adiciona uma linha em branco
            self.gridVolumes.SetCellValue(self.gridVolumes.GetNumberRows() - 1, 0,
                                         str(volume[0]))  # adicione o id da Volumes
            self.gridVolumes.SetCellValue(self.gridVolumes.GetNumberRows() - 1, 1,
                                         volume[1])  # adiciona o nome da Volumes
            self.gridVolumes.SetReadOnly(self.gridVolumes.GetNumberRows() - 1, 0,
                                        True)  # Informa que a coluna 0(ID) é somente leitura

    # Handlers for FrameVolumes events.
    def fecharFrame(self, event):
        self.Show(False)
