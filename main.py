from init import createApp
from  database import createDatabase
app=createApp()
createDatabase()
if __name__ == "__main__":
    app.run(debug=True)