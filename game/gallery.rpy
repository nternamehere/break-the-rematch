init python:

    g = Gallery()

    g.button("reika_sex1_inside")
    g.image("reika_sex1-1")
    g.image("reika_sex1-2")
    g.image("reika_sex1-3")
    g.image("reika_sex1-4")
    g.image("reika_sex1-5")
    g.image("reika_sex1-6")
    g.image("reika_sex1-7")
    g.image("reika_sex1-8_inside-1")
    g.image("reika_sex1-8_inside-2")
    g.image("reika_sex1-8_inside-3")
    g.unlock("reika_sex1-8_inside-3")

    g.button("reika_sex1_outside")
    g.image("reika_sex1-1")
    g.image("reika_sex1-2")
    g.image("reika_sex1-3")
    g.image("reika_sex1-4")
    g.image("reika_sex1-5")
    g.image("reika_sex1-6")
    g.image("reika_sex1-7")
    g.image("reika_sex1-8_outside-1")
    g.image("reika_sex1-8_outside-2")
    g.image("reika_sex1-8_outside-3")
    g.unlock("reika_sex1-8_outside-3")

    g.button("dawn3")
    g.image("dawn3")
    g.unlock("dawn3")

    g.transition = dissolve
    g.locked_button = "gui/button/gallery_locked.png"
    g.hover_border = "gui/button/gallery_hover.png"
    g.idle_border = "gui/button/gallery_idle.png"

screen gallery:
    tag menu

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(_("Gallery")):

        fixed:

            grid 3 2:

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                add g.make_button("reika_sex1_inside", "images/gallery/gallery_reika_sex1_inside.png")
                add g.make_button("reika_sex1_outside", "images/gallery/gallery_reika_sex1_outside.png")
                add g.make_button("dawn3", "images/CGs/Reika/Sex_Scene_1/reika_sex1-1.png", xalign=0.5, yalign=0.5)

                add g.make_button("dawn3", "images/CGs/Reika/Sex_Scene_1/reika_sex1-1.png", xalign=0.5, yalign=0.5)
                add g.make_button("dawn3", "images/CGs/Reika/Sex_Scene_1/reika_sex1-1.png", xalign=0.5, yalign=0.5)
                add g.make_button("dawn3", "images/CGs/Reika/Sex_Scene_1/reika_sex1-1.png", xalign=0.5, yalign=0.5)
