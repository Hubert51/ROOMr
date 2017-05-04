import web 
render = web.template.render("templates/")
name = 'Bob'    


urls= (
    '/', 'index'
)

class index:
    def GET(self):
    	name = "Bob"
        return render.index(name)



if __name__ == "__main__":

    app = web.application(urls , globals())
    db = web.database(dbn='mysql', user='ruijiegeng@gmail.com', pw='G12345grj', db='ROOMr')
    app.run() 




