"""Subclass of FrameMarca, which is generated by wxFormBuilder."""

import wx
import guiperfumes
import db

# Implementing FrameMarca
class FrameMarca(guiperfumes.FrameMarca):
	def __init__( self, parent ):
		guiperfumes.FrameMarca.__init__( self, parent )
		self.atualizarGrid()
	# Handlers for FrameMarca events.
	def adicionarMarca( self, event ):
		nome=self.txtNome.GetValue() #Recupera o conteúdo da caixa de texto
		db.inserirMarca(nome) #Chama a função inserir marca do arquivo db.py
		#Exibe uma mensagem ao usuário confirmado o sucesso na inserção
		wx.MessageBox(message="Marca Inserida com Sucesso",caption="SisPerfumes",style=wx.OK,parent=self)
		self.atualizarGrid()#Atualiza o grid com a relação de marcas
	def fecharFrame( self, event ):
		self.Show(False)
	#Essa função é chamada quando o usuário edita o conteúdo de uma célula do meu grid
	def atualizarMarca( self, event ):
		nome_marca=self.gridMarcas.GetCellValue(event.GetRow(),event.GetCol()) #Recupera o nome da marca editado
		if (nome_marca): #Se o conteúdo não for vazio, faça
			id_marca=int(self.gridMarcas.GetCellValue(event.GetRow(),0))#Pegue na linha editada, o conteúdo da primeira coluna
			db.atualizarMarca(id_marca,nome_marca) #Chame a função para atualizar uma marca
			wx.MessageBox(message="Marca Atualizada com Sucesso",caption="SysPerfumes",style=wx.OK,parent=self)
	def atualizarGrid(self):
		if (self.gridMarcas.GetNumberRows()>0):
			self.gridMarcas.DeleteRows(0,self.gridMarcas.GetNumberRows()) #Limpa a tabela
		marcas=db.listarMarca() #Chama a função listar marcas, retornando a lista de marcas existentes
		for marca in marcas:
			self.gridMarcas.AppendRows(1)#Adiciona uma linha em branco
			self.gridMarcas.SetCellValue(self.gridMarcas.GetNumberRows()-1,0,str(marca[0])) #adicione o id da marca
			self.gridMarcas.SetCellValue(self.gridMarcas.GetNumberRows() - 1, 1, marca[1]) #adiciona o nome da marca
			self.gridMarcas.SetReadOnly(self.gridMarcas.GetNumberRows() - 1, 0, True) #Informa que a coluna 0(ID) é somente leitura


