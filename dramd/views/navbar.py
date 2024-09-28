import reflex as rx


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(rx.text(text, size="4", weight="medium"), href=url)


def navbar() -> rx.Component:
    return rx.box(
        # rx.desktop_only(
        #     rx.hstack(
        #         rx.hstack(
        #             rx.badge(
        #                 rx.icon(tag="glass-water", size=28),
        #                 rx.heading("dramd", size="6"),
        #                 radius="large",
        #                 # align="center",
        #                 # color_scheme="purple",
        #                 # variant="surface",
        #                 padding="0.65rem",
        #             ),
        #             align_items="center",
        #         ),
        #         rx.hstack(
        #             navbar_link("Home", "/#"),
        #             navbar_link("About", "/#"),
        #             navbar_link("Pricing", "/#"),
        #             navbar_link("Contact", "/#"),
        #             spacing="5",
        #         ),
        #         rx.hstack(
        #             rx.button(
        #                 "Sign Up",
        #                 size="3",
        #                 variant="outline",
        #             ),
        #             rx.button("Log In", size="3"),
        #             spacing="4",
        #             justify="end",
        #         ),
        #         justify="between",
        #         align_items="center",
        #     ),
        # ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.icon(tag="glass-water", size=28),
                    rx.heading("dramd", size="6"),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30)),
                    rx.menu.content(
                        rx.menu.item("Home"),
                        rx.menu.item("About"),
                        rx.menu.separator(),
                        rx.menu.item("Log in"),
                        rx.menu.item("Sign up"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )
