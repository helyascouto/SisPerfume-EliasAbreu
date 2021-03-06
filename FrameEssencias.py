"""Subclass of FrameEssencias, which is generated by wxFormBuilder."""

import wx
import guiperfumes
import db


# Implementing FrameEssencias
class FrameEssencias(guiperfumes.FrameEssencias):
    def __init__(self, parent):
        guiperfumes.FrameEssencias.__init__(self, parent)
        self.atualizarGridEssencias()

    # Handlers for FrameEssencias events.
    def adicionarEssencia(self, event):
        nome = self.txtNome.GetValue()  # Recupera o conteúdo da caixa de texto
        db.inserirEssencia(nome)  # Chama a função inserir essencias do arquivo db.py
        # Exibe uma mensagem ao usuário confirmado o sucesso na inserção
        wx.MessageBox(message="Essencia Inserida com Sucesso", caption="SisPerfumes", style=wx.OK, parent=self)
        self.atualizarGridEssencias()  # Atualiza o grid com a relação de essencias

    def atualizarEssencia(self, event):
        nome_essecias = self.gridEssencias.GetCellValue(event.GetRow(),
                                                        event.GetCol())  # Recupera o nome da essencias editado

        if (nome_essecias):  # Se o conteúdo não for vazio, faça
            id_essencia = int(self.gridEssencias.GetCellValue(event.GetRow(),
                                                              0))  # Pegue na linha editada, o conteúdo da primeira coluna
        db.atualizarEssencia(id_essencia, nome_essecias)  # Chame a função para atualizar uma essencias
        wx.MessageBox(message="Essencia Atualizada com Sucesso", caption="SysPerfumes", style=wx.OK,
                      parent=self)

    def atualizarGridEssencias(self):
        if (self.gridEssencias.GetNumberRows() > 0):
            self.gridEssencias.DeleteRows(0, self.gridEssencias.GetNumberRows())  # Limpa a tabela

        essencias = db.listarEssencias()  # Chama a função listar essencias, retornando a lista de essencias existentes

        for essencias in essencias:
            self.gridEssencias.AppendRows(1)  # Adiciona uma linha em branco
            self.gridEssencias.SetCellValue(self.gridEssencias.GetNumberRows() - 1, 0,
                                            str(essencias[0]))  # adicione o id da essencias
            self.gridEssencias.SetCellValue(self.gridEssencias.GetNumberRows() - 1, 1,
                                            essencias[1])  # adiciona o nome da essencias
            self.gridEssencias.SetReadOnly(self.gridEssencias.GetNumberRows() - 1, 0,
                                           True)  # Informa que a coluna 0(ID) é somente leitura

    def fecharFrame(self, event):
        self.Show(False)
