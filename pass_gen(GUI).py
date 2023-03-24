import wx
import wx.lib.dialogs

from WORDS.PGCW import pgcw_service as pgcws
from WORDS.PGCWRW import pgcwrw_service as pgcwrws
from WORDS.PGPEW import pgpew_service as pgpews
from WORDS.PGPW import pgpw_service as pgpws


class PasswordGenerator(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Dayana Dictionary Builder')
        panel = wx.Panel(self)

        # Create the controls
        method_label = wx.StaticText(panel, label='Method:', pos=(20, 20))
        self.method_box = wx.ComboBox(panel, pos=(210, 20), choices=[
                                      'pgcw', 'pgcwrw', 'pgpew', 'pgpw'])

        start_label = wx.StaticText(panel, label='Start Range:', pos=(20, 60))
        self.start_input = wx.TextCtrl(panel, pos=(210, 60))

        end_label = wx.StaticText(panel, label='End Range:', pos=(20, 100))
        self.end_input = wx.TextCtrl(panel, pos=(210, 100))

        words_label = wx.StaticText(
            panel, label='Words(Enter letters with spaces):', pos=(5, 140))
        self.words_input = wx.TextCtrl(panel, pos=(210, 140))

        self.save_button = wx.Button(panel, label='Save As', pos=(20, 180))
        self.save_button.Bind(wx.EVT_BUTTON, self.on_save)

        self.generate_button = wx.Button(
            panel, label='Generate', pos=(210, 180))
        self.generate_button.Bind(wx.EVT_BUTTON, self.on_generate)

        self.result_label = wx.StaticText(panel, label='', pos=(160, 240))
        self.result_len = wx.StaticText(panel, label='', pos=(20, 240))
        self.result_output = wx.TextCtrl(panel, pos=(10, 260), size=(
            360, 100), style=wx.TE_READONLY | wx.TE_MULTILINE)

        # Set the size and show the frame
        self.SetSize((400, 400))
        self.Show()

    def on_save(self, event):
        save_dialog = wx.FileDialog(
            self, message="Save file", defaultFile="passwords.txt", wildcard="Text files (*.txt)|*.txt")
        if save_dialog.ShowModal() == wx.ID_OK:
            with open(save_dialog.GetPath(), 'w') as f:
                f.write(self.result_output.GetValue())
        save_dialog.Destroy()

    def on_generate(self, event):
        method = self.method_box.GetValue()
        start_range = self.start_input.GetValue()
        end_range = self.end_input.GetValue()
        words = self.words_input.GetValue()
        words = str(words)
        words_list = words.split(" ")

        # Validate the inputs
        if not start_range.isdigit():
            self.result_label.SetLabel(
                'Please enter a number to start the range')
            return
        if not end_range.isdigit():
            self.result_label.SetLabel(
                'Please enter a number to end the range')
            return

        start_range = int(start_range)
        end_range = int(end_range)

        # Generate the passwords
        if method == 'pgcw':
            passwords = pgcws.combinations_functions(
                start_range=start_range, end_range=end_range, word_list=words_list)
            show_len = pgcws.show_len()
        elif method == 'pgcwrw':
            passwords = pgcwrws.combinations_with_replacement_function(
                start_range=start_range, end_range=end_range, word_list=words_list)
            show_len = pgcwrws.show_len()
        elif method == 'pgpew':
            passwords = pgpews.permutations_function(
                start_range=start_range, end_range=end_range, word_list=words_list)
            show_len = pgpews.show_len()
        elif method == 'pgpw':
            passwords = pgpws.product_function(
                start_range=start_range, end_range=end_range, word_list=words_list)
            show_len = pgpws.show_len()

        # Display the passwords
        if passwords:
            result_text = (passwords)
            self.result_output.SetLabel(result_text)
            # Reset label
            self.result_label.SetLabel("")

            # Display the number of words
            self.result_len.SetLabel(f"{show_len} words were generated")
        else:
            self.result_label.SetLabel('No passwords generated')
            self.result_output.SetLabel("")
            self.result_len.SetLabel("")


if __name__ == '__main__':
    app = wx.App()
    PasswordGenerator()
    app.MainLoop()
