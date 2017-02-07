import datetime
import sublime_plugin
class AddInfo(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet",
            {
                "contents": "--[[""\n"
                " * @Version:     1.0""\n"
                " * @Author:      GitHubNull""\n"
                " * @Email:       641570479@qq.com""\n"
                " * @github:      GitHubNull""\n"
                " * @Description: This is about...""\n"
                " * @DateTime:    "  "%s"  %datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") +"\n"
               	"--]]"
            }
        )
