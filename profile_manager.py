From textual.app import App, ComposeResult

From textual.containers import Horizontal, Vertical

From textual.widgets import Header, Footer, Button, Static, ListView, ListItem



PROFILE_ACTIONS = [“Run”, “Edit”, “Delete”, “Export”, “Quit”]

DUMMY_PROFILES = [“apache-lfi-test”, “solr-rce-poc”, “log4shell-lab”]



Class ProfileManager(App):

    CSS_PATH = “profile_manager.tcss”



    Selected_profile: Static | None = None



    Def compose(self) -> ComposeResult:

        Yield Header(show_clock=True)

        Yield Static(“Ghostshell Profile Manager”, id=”title”)



        Yield Horizontal(

            Vertical(

                ListView(

                    *[ListItem(Static(name)) for name in DUMMY_PROFILES],

                    Id=”profile_list”

                ),

                Id=”profiles_pane”

            ),

            Vertical(

                ListView(

                    *[ListItem(Button(action, id=action.lower(), disabled=True)) for action in PROFILE_ACTIONS],

                    Id=”menu”

                ),

                Id=”actions_pane”

            )

        )

        Yield Footer()



    Def on_mount(self) -> None:

        “””Set the initial state of the action buttons.”””

        Self.query_one(“#quit”, Button).disabled = False



    Def on_list_view_selected(self, event: ListView.Selected) -> None:

        “””Handle profile selection.”””

        Self.selected_profile = event.item.query_one(Static)

        Self.console.log(f”Selected profile: {self.selected_profile.renderable}”)



        # Enable/disable buttons based on selection

        For button in self.query(“Button”):

            If button.id != “quit”:

                Button.disabled = False



    Def on_button_pressed(self, event: Button.Pressed) -> None:

        Action = event.button.id

        If action == “run”:

            If self.selected_profile:

                Self.run_profile(self.selected_profile.renderable)

        Elif action == “quit”:

            Self.exit()

        Else:

            Self.console.log(f”Action ‘{action}’ is not implemented yet.”)



    Def run_profile(self, profile_name):

        Self.console.log(f”Attempting to run profile: {profile_name}”)

        # In a real app, you would add logic here to read the YAML,

        # run docker commands, and execute the PoC script.

        # For now, we just log to the console.



If __name__ == “__main__”:

    ProfileManager().run()
