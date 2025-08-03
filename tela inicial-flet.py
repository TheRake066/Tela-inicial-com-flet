import flet as ft

def main(page: ft.Page):
    page.bgcolor = '#8ab9eb'
    page.theme_mode = ft.ThemeMode.DARK
    page.title = 'aplicativo para celular' # Barra de titulo
    page.window.width = 450 # Tamanho das janelas
    page.window.height = 700
    page.window.maximizable = False # Desativa tela cheia
    page.vertical_alignment = 'center' # Centraliza plano de fundo
    page.horizontal_alignment = 'center'
    
    # cria funções para botões 
    def btn_editar(e):
        _stack_main.controls.clear()
        _stack_main.update()
        
        _stack_main.controls.append(editar)
        _stack_main.update()

    def btn_config(e):
        _stack_main.controls.clear()
        _stack_main.update()
        
        _stack_main.controls.append(config)
        _stack_main.update()
   
    def btn_favorito(e):
        _stack_main.controls.clear()
        _stack_main.update()

        _stack_main.controls.append(favorito)
        _stack_main.update()

    def btn_principal(e):
        _stack_main.controls.clear()
        _stack_main.update()

        _stack_main.controls.append(_main)
        _stack_main.update()

    def btn_procurar(e):
        _stack_main.controls.clear()
        _stack_main.update()

        _stack_main.controls.append(procurar)
        _stack_main.update() 
    
    # adiciona e centraliza um botão para a pagina principal
    page.floating_action_button = ft.FloatingActionButton(icon=ft.Icons.ADD, bgcolor='blue', on_click=btn_principal)
    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED
    
    # adiciona uma barra de navegação
    page.bottom_appbar = ft.BottomAppBar(
        bgcolor='#F6F6F6FF',
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            # Customizando os botões da barra
            controls=[
                ft.IconButton(icon=ft.Icons.EDIT, icon_color=ft.Colors.BLUE, icon_size=26, on_click=btn_editar),
                ft.IconButton(icon=ft.Icons.SETTINGS, icon_color=ft.Colors.BLUE, icon_size=26, on_click=btn_config),
                ft.Container(expand=True),
                ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.BLUE, icon_size=26, on_click=btn_procurar),
                ft.IconButton(icon=ft.Icons.FAVORITE, icon_color=ft.Colors.BLUE, icon_size=26, on_click=btn_favorito)
            ]
        ),
    )
    
    # Container principal
    
    _main = ft.Container(
        width=400,
        height=600,
        bgcolor='#F6F6F6FF',
        border_radius=16,
        alignment=ft.alignment.center,
        shadow=ft.BoxShadow(blur_radius=20,color=ft.Colors.with_opacity(opacity=0.5, color='black')),
        content=ft.Text(
            value='INICIO',
            color='black',
            size=32
        )
    )
    # editar container

    editar = ft.Container(
        width=400,
        height=600,
        bgcolor='#F6F6F6FF',
        border_radius=16,
        alignment=ft.alignment.center,
        shadow=ft.BoxShadow(blur_radius=20,color=ft.Colors.with_opacity(opacity=0.5, color='black')),
        content=ft.Text(
            value='EDITAR',
            color='black',
            size=32
        )
    ) 
    # config container
    
    config = ft.Container(
        width=400,
        height=600,
        bgcolor='#F6F6F6FF',
        border_radius=16,
        alignment=ft.alignment.center,
        shadow=ft.BoxShadow(blur_radius=20,color=ft.Colors.with_opacity(opacity=0.5, color='black')),
        content=ft.Text(
            value='CONFIGURAÇÕES',
            color='black',
            size=32
        )
    ) 
    
    # Favorito container
    favorito = ft.Container(
        width=400,
        height=600,
        bgcolor='#F6F6F6FF',
        border_radius=16,
        alignment=ft.alignment.center,
        shadow=ft.BoxShadow(blur_radius=20,color=ft.Colors.with_opacity(opacity=0.5, color='black')),
        content=ft.Text(
            value='FAVORITO',
            color='black',
            size=3        )
    ) 
    
    # Procurar Container
    procurar = ft.Container(
        width=400,
        height=600,
        bgcolor='#F6F6F6FF',
        border_radius=18,        
        alignment=ft.alignment.top_left,
        shadow=ft.BoxShadow(blur_radius=20,color=ft.Colors.with_opacity(opacity=0.5, color='black')),
        content=ft.TextField(
            border_radius=18,
            label='digite algo: ',
            width=900,
            height=400,
            text_style=ft.TextStyle(
                color='black',
                size=19
            )
        )
    ) 

    # Stack principal

    _stack_main = ft.Stack(
        controls=[
            _main
        ]
    )

    page.add(_stack_main)

ft.app(target=main)
