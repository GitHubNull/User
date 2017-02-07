import datetime
import sublime_plugin
class AddComment(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet",
            {
                "contents": 
                " * @Author:      GitHubNull""\n"
                " * Description: This is about...""\n"
                " * DateTime:    "  "%s"  %datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") +"\n"
            }
        )
