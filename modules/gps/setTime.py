import web
import os

urls = (
    '/', 'index'
)

class index(object):

	@classmethod
	def GET(self):
		data = web.input()
		if data.data != 'NaN':
			with open('time.json', 'w') as file_:
				file_.write(data.data)
				# Update system time
				os.system("date +%s -s @" + str(data.data))

		return data.data

if __name__ == "__main__":

	app = web.application(urls, globals())
	app.run()