import flet as ft

Path_to_file_data = str

def main(page: ft.Page):
    page.title = "Machine Diagnostic"
    page.window_height = 820
    page.window_width = 1280
    page.window_resizable = False
    page.bgcolor = "Grey"
    def pick_files_result(e: ft.FilePickerResultEvent):
        a = e.files

        global Path_to_file_data
        Path_to_file_data = a[0].path

        selected_files.value += (
           (a[0].name) if e.files else "Вы отменили выбор!"
        )
        selected_files.update()
        page.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text("Вы выбрали файл: ",color="Blue")
    c3 = ft.Container(
 
        content=selected_files,
        bgcolor="Black",
        padding=10,
        border_radius=5
    )

    page.overlay.append(pick_files_dialog)

    img = ft.Image(
        src=f"D:\Proga\хакатон Eestech\MainFon.png",
        width=700,
        height=500,
        fit=ft.ImageFit.FILL,
    )

    k1 = ft.Text("Двигатель Внутреннего Сгорания", bgcolor = "Green")
    k2 = ft.Text("Коробка Переключения Передач", bgcolor = "Green")

    k4 = ft.Text("Тормозная система", bgcolor = "Green")
    k5 = ft.Text("Гидравлика", bgcolor = "Green")


    c1 = ft.Container(
        content = 
                ft.ElevatedButton(
                    "Загрузить данные с датчиков трактора",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(allow_multiple=True),
                ),
                
        #bgcolor=ft.colors.YELLOW,
        padding=5,
        ink = True,  
    )
    c2 = ft.Container(
        content=ft.ElevatedButton(
                    "Обработать", 
                    icon = ft.icons.WORK,
                    on_click=lambda e: print("Обработка моделью, путь", Path_to_file_data)),
        #bgcolor=ft.colors.RED,
        padding=5,
        ink = True,            
    )

    lv =ft.ListView(expand=True, spacing=10,height=400,width=420)
    lvkont = ft.Container(content=lv,height=500,width=400,bgcolor="White")
    for i in range(25):
        lv.controls.append(ft.Text(f"Line {i}",color="Black"))


    
    def route_change(e):
        page.views.clear()
        page.views.append(
            ft.View("1page",
                    bgcolor="Grey",
                    controls=[
                        ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[c1,c2]),
                        ft.Row(controls = [c3]),
                        ft.Row(controls=[k4,k5], alignment=ft.MainAxisAlignment.SPACE_AROUND),
                        ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls= [img]),
                        ft.Row(controls=[k1,k2], alignment=ft.MainAxisAlignment.SPACE_AROUND),
                        ft.Row(alignment=ft.MainAxisAlignment.CENTER,controls=[ft.Container(content = ft.ElevatedButton('К точечным данным', bgcolor= "DarkBlue", on_click =lambda _: page.go("2page")),)])
                    ]
            ),)
        if page.route == "2page":
            page.views.append(
            ft.View("2page",
                    bgcolor="Grey",
                    controls=[
                        ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[c1,c2]),
                        ft.Row(controls = [c3]),
                        ft.Row(controls=[ft.Text('Пролистываемый список',color="Black")]),
                        ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls= [lvkont, img]),
                        ft.Row(alignment=ft.MainAxisAlignment.CENTER,controls=[ft.Container(content = ft.ElevatedButton('К основным узлам машины', bgcolor= "DarkBlue", on_click =lambda _: page.go("1page")),)])
                    ])
        )
        page.update()
    
    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route)
        
        

ft.app(target=main)

