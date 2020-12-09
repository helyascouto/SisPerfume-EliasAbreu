# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class FrameMarca
###########################################################################

class FrameMarca ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Marcas", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Descrição:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.txtNome = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.txtNome, 1, wx.ALL, 5 )

		self.btnAdicionar = wx.Button( self, wx.ID_ANY, u"Adicionar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.btnAdicionar, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.gridMarcas = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.gridMarcas.CreateGrid( 0, 2 )
		self.gridMarcas.EnableEditing( True )
		self.gridMarcas.EnableGridLines( True )
		self.gridMarcas.EnableDragGridSize( False )
		self.gridMarcas.SetMargins( 0, 0 )

		# Columns
		self.gridMarcas.SetColSize( 0, 30 )
		self.gridMarcas.SetColSize( 1, 300 )
		self.gridMarcas.EnableDragColMove( False )
		self.gridMarcas.EnableDragColSize( True )
		self.gridMarcas.SetColLabelSize( 30 )
		self.gridMarcas.SetColLabelValue( 0, u"ID" )
		self.gridMarcas.SetColLabelValue( 1, u"Nome" )
		self.gridMarcas.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.gridMarcas.EnableDragRowSize( True )
		self.gridMarcas.SetRowLabelSize( 80 )
		self.gridMarcas.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.gridMarcas.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.gridMarcas.SetToolTip( u"Pressione Enter para atualizar uma Marca" )

		bSizer3.Add( self.gridMarcas, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.fecharFrame )
		self.btnAdicionar.Bind( wx.EVT_BUTTON, self.adicionarMarca )
		self.gridMarcas.Bind( wx.grid.EVT_GRID_CELL_CHANGED, self.atualizarMarca )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def fecharFrame( self, event ):
		event.Skip()

	def adicionarMarca( self, event ):
		event.Skip()

	def atualizarMarca( self, event ):
		event.Skip()


###########################################################################
## Class FrameVolumes
###########################################################################

class FrameVolumes ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Volumes", pos = wx.DefaultPosition, size = wx.Size( 438,355 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Descrição:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.txtNome = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.txtNome, 1, wx.ALL, 5 )

		self.btnAdicionar = wx.Button( self, wx.ID_ANY, u"Adicionar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnAdicionar.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.btnAdicionar.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer2.Add( self.btnAdicionar, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.gridVolumes = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.gridVolumes.CreateGrid( 0, 2 )
		self.gridVolumes.EnableEditing( True )
		self.gridVolumes.EnableGridLines( True )
		self.gridVolumes.SetGridLineColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.gridVolumes.EnableDragGridSize( False )
		self.gridVolumes.SetMargins( 0, 0 )

		# Columns
		self.gridVolumes.SetColSize( 0, 30 )
		self.gridVolumes.SetColSize( 1, 300 )
		self.gridVolumes.EnableDragColMove( False )
		self.gridVolumes.EnableDragColSize( True )
		self.gridVolumes.SetColLabelSize( 30 )
		self.gridVolumes.SetColLabelValue( 0, u"ID" )
		self.gridVolumes.SetColLabelValue( 1, u"Nome" )
		self.gridVolumes.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.gridVolumes.EnableDragRowSize( True )
		self.gridVolumes.SetRowLabelSize( 80 )
		self.gridVolumes.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.gridVolumes.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.gridVolumes.SetLabelTextColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		# Cell Defaults
		self.gridVolumes.SetDefaultCellBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		self.gridVolumes.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.gridVolumes.SetToolTip( u"Pressione Enter para atualizar uma Marca" )

		bSizer3.Add( self.gridVolumes, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.fecharFrame )
		self.btnAdicionar.Bind( wx.EVT_BUTTON, self.adicionarVolume )
		self.gridVolumes.Bind( wx.grid.EVT_GRID_CELL_CHANGED, self.atualizarVolume )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def fecharFrame( self, event ):
		event.Skip()

	def adicionarVolume( self, event ):
		event.Skip()

	def atualizarVolume( self, event ):
		event.Skip()


###########################################################################
## Class FramePrincipal
###########################################################################

class FramePrincipal ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Sistema de Gestão de Perfumes", pos = wx.DefaultPosition, size = wx.Size( 1207,623 ), style = wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.menuMarcas = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Marcas", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.menuMarcas )

		self.menuEssencias = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Essências", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.menuEssencias )

		self.menuFixacoes = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Fixações", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.menuFixacoes )

		self.menuVolume = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Volumes", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.menuVolume )

		self.m_menubar1.Append( self.m_menu1, u"Cadastros Básicos" )

		self.m_menu2 = wx.Menu()
		self.menuPerfumes = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Registros", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.menuPerfumes )

		self.menuPerfumeEssencia = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Adicionar Essencias", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.menuPerfumeEssencia )

		self.m_menubar1.Append( self.m_menu2, u"Perfumes" )

		self.m_menu3 = wx.Menu()
		self.menuSobre = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Sobre", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.menuSobre )

		self.menuSair = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Sair", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.menuSair )

		self.m_menubar1.Append( self.m_menu3, u"Ajuda" )

		self.SetMenuBar( self.m_menubar1 )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_bitmap4 = wx.StaticBitmap( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.Bitmap( u"Imagens/fundo.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.TRANSPARENT_WINDOW )
		self.m_bitmap4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_bitmap4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		sbSizer2.Add( self.m_bitmap4, 0, wx.ALL, 1 )


		self.SetSizer( sbSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.fecharFramePrincipal )
		self.Bind( wx.EVT_MENU, self.abrirMarca, id = self.menuMarcas.GetId() )
		self.Bind( wx.EVT_MENU, self.AbrirEssencias, id = self.menuEssencias.GetId() )
		self.Bind( wx.EVT_MENU, self.abrirFixacoes, id = self.menuFixacoes.GetId() )
		self.Bind( wx.EVT_MENU, self.abrirVolumes, id = self.menuVolume.GetId() )
		self.Bind( wx.EVT_MENU, self.abrirPerfume, id = self.menuPerfumes.GetId() )
		self.Bind( wx.EVT_MENU, self.fecharApp, id = self.menuSair.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def fecharFramePrincipal( self, event ):
		event.Skip()

	def abrirMarca( self, event ):
		event.Skip()

	def AbrirEssencias( self, event ):
		event.Skip()

	def abrirFixacoes( self, event ):
		event.Skip()

	def abrirVolumes( self, event ):
		event.Skip()

	def abrirPerfume( self, event ):
		event.Skip()

	def fecharApp( self, event ):
		event.Skip()


###########################################################################
## Class FramePerfumes
###########################################################################

class FramePerfumes ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Perfumes", pos = wx.DefaultPosition, size = wx.Size( 1220,364 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.gridPerfumes = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.gridPerfumes.CreateGrid( 0, 7 )
		self.gridPerfumes.EnableEditing( True )
		self.gridPerfumes.EnableGridLines( True )
		self.gridPerfumes.EnableDragGridSize( False )
		self.gridPerfumes.SetMargins( 0, 0 )

		# Columns
		self.gridPerfumes.SetColSize( 0, 30 )
		self.gridPerfumes.SetColSize( 1, 200 )
		self.gridPerfumes.SetColSize( 2, 100 )
		self.gridPerfumes.SetColSize( 3, 200 )
		self.gridPerfumes.SetColSize( 4, 200 )
		self.gridPerfumes.SetColSize( 5, 200 )
		self.gridPerfumes.SetColSize( 6, 200 )
		self.gridPerfumes.EnableDragColMove( False )
		self.gridPerfumes.EnableDragColSize( True )
		self.gridPerfumes.SetColLabelSize( 30 )
		self.gridPerfumes.SetColLabelValue( 0, u"ID" )
		self.gridPerfumes.SetColLabelValue( 1, u"Nome" )
		self.gridPerfumes.SetColLabelValue( 2, u"Quantidade" )
		self.gridPerfumes.SetColLabelValue( 3, u"Volume" )
		self.gridPerfumes.SetColLabelValue( 4, u"Marca" )
		self.gridPerfumes.SetColLabelValue( 5, u"Fixação" )
		self.gridPerfumes.SetColLabelValue( 6, u"Essencias" )
		self.gridPerfumes.SetColLabelValue( 7, wx.EmptyString )
		self.gridPerfumes.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.gridPerfumes.EnableDragRowSize( True )
		self.gridPerfumes.SetRowLabelSize( 80 )
		self.gridPerfumes.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.gridPerfumes.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer21.Add( self.gridPerfumes, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer20.Add( bSizer21, 1, wx.EXPAND, 5 )

		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )

		self.btnAdicionar = wx.Button( self, wx.ID_ANY, u"Adicionar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.btnAdicionar, 1, wx.ALL, 5 )

		self.btnSalvar = wx.Button( self, wx.ID_ANY, u"Salvar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.btnSalvar, 1, wx.ALL, 5 )


		bSizer20.Add( bSizer22, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer20 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.fecharFrame )
		self.Bind( wx.EVT_SHOW, self.exibirFrame )
		self.btnAdicionar.Bind( wx.EVT_BUTTON, self.adicionarLinha )
		self.btnSalvar.Bind( wx.EVT_BUTTON, self.salvarPerfume )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def fecharFrame( self, event ):
		event.Skip()

	def exibirFrame( self, event ):
		event.Skip()

	def adicionarLinha( self, event ):
		event.Skip()

	def salvarPerfume( self, event ):
		event.Skip()


###########################################################################
## Class FrameFixacoes
###########################################################################

class FrameFixacoes ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Fixacoes", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Descrição:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.txtNome = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.txtNome, 1, wx.ALL, 5 )

		self.btnAdicionar = wx.Button( self, wx.ID_ANY, u"Adicionar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.btnAdicionar, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.gridFixacoes = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.gridFixacoes.CreateGrid( 0, 2 )
		self.gridFixacoes.EnableEditing( True )
		self.gridFixacoes.EnableGridLines( True )
		self.gridFixacoes.EnableDragGridSize( False )
		self.gridFixacoes.SetMargins( 0, 0 )

		# Columns
		self.gridFixacoes.SetColSize( 0, 30 )
		self.gridFixacoes.SetColSize( 1, 300 )
		self.gridFixacoes.EnableDragColMove( False )
		self.gridFixacoes.EnableDragColSize( True )
		self.gridFixacoes.SetColLabelSize( 30 )
		self.gridFixacoes.SetColLabelValue( 0, u"ID" )
		self.gridFixacoes.SetColLabelValue( 1, u"Nome" )
		self.gridFixacoes.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.gridFixacoes.EnableDragRowSize( True )
		self.gridFixacoes.SetRowLabelSize( 80 )
		self.gridFixacoes.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.gridFixacoes.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.gridFixacoes.SetToolTip( u"Pressione Enter para atualizar uma Marca" )

		bSizer3.Add( self.gridFixacoes, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnAdicionar.Bind( wx.EVT_BUTTON, self.adicionarFixacoes )
		self.gridFixacoes.Bind( wx.grid.EVT_GRID_CELL_CHANGED, self.atualizarFixacoes )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def adicionarFixacoes( self, event ):
		event.Skip()

	def atualizarFixacoes( self, event ):
		event.Skip()


###########################################################################
## Class FrameEssencias
###########################################################################

class FrameEssencias ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Essencias", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Descrição:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.txtNome = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.txtNome, 1, wx.ALL, 5 )

		self.BtnAdicionarEssencias = wx.Button( self, wx.ID_ANY, u"Adicionar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.BtnAdicionarEssencias, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.gridEssencias = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.gridEssencias.CreateGrid( 0, 2 )
		self.gridEssencias.EnableEditing( True )
		self.gridEssencias.EnableGridLines( True )
		self.gridEssencias.EnableDragGridSize( False )
		self.gridEssencias.SetMargins( 0, 0 )

		# Columns
		self.gridEssencias.SetColSize( 0, 30 )
		self.gridEssencias.SetColSize( 1, 300 )
		self.gridEssencias.EnableDragColMove( False )
		self.gridEssencias.EnableDragColSize( True )
		self.gridEssencias.SetColLabelSize( 30 )
		self.gridEssencias.SetColLabelValue( 0, u"ID" )
		self.gridEssencias.SetColLabelValue( 1, u"Nome" )
		self.gridEssencias.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.gridEssencias.EnableDragRowSize( True )
		self.gridEssencias.SetRowLabelSize( 80 )
		self.gridEssencias.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.gridEssencias.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.gridEssencias.SetToolTip( u"Pressione Enter para atualizar uma Marca" )

		bSizer3.Add( self.gridEssencias, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.BtnAdicionarEssencias.Bind( wx.EVT_BUTTON, self.adicionarEssencia )
		self.gridEssencias.Bind( wx.grid.EVT_GRID_CELL_CHANGED, self.atualizarEssencia )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def adicionarEssencia( self, event ):
		event.Skip()

	def atualizarEssencia( self, event ):
		event.Skip()


