bundle_path = getBundlePath()
tmpdir = os.path.join(bundle_path, "autocapture")
if not os.path.exists(tmpdir):
    os.mkdir(tmpdir)

tap_to_start_screen = "1496527514315.png"
help = "1496465082667.png"
arena = "1496517894613.png"
arena2 = "arena2.png"
world_icon = "world_icon.png"
vortex_icon = "vortex_icon.png"

map_vortex = "map_vortex.png"
map_grandshelt = "map_grandshelt.png"
map_grandshelt_map_grandshelt_isles = "map_grandshelt_map_grandshelt_isles.png"
map_gi_ordol_port = "map_gi_ordol_port.png"
map_gi_earth_shrine = "map_gi_earth_shrine.png"
earth_shrine_entrance = "earth_shrine_entrance.png"
earth_shrine_exit = "earth_shrine_exit.png"

screen = Screen()
#print switchApp("MEmu App Player")
app = switchApp("FFBESnark")
app.focus()
reg = app.focusedWindow()
print reg
#reg.highlight(10)

# topLeft = find("1496518701262.png")
# bottomRight = find("1496518729383.png")
# reg = Region( topLeft.x, topLeft.y,
#         bottomRight.x - topLeft.x + bottomRight.w +10,
#         bottomRight.y - topLeft.y + bottomRight.h +10
#         # )
# # reg.highlight(1)
# # print topLeft, bottomRight, reg

state_login = "state_login.png"
state_login_ok = "state_login_ok.png"
back_button = "1496519298720.png"
arena_setup = "1496519329070.png"
arena_has_orb = "1496519345959.png"
arena_rules_ok = "arena_rules_ok.png"
arena_opponent_row = "arena_opponent_row.png"

adventure_next = "adventure_next.png"
adventure_select_friend_page = "adventure_select_friend_page.png"
adventure_party_select_page = "adventure_party_select_page.png"

homescreen = "1496519783253.png"
arena_page = "arena_page.png"
interstitial_page = "interstitial_page.png"
interstitial_loading = "interstitial_loading.png"
raid_event = "raid_event.png"
raid_event_has_orb = "raid_event_has_orb.png"


# units
combat_group_top = "combat_group_top.png"
combat_group_bottom = "combat_group_bottom.png"
combat_group_sword_icon = "combat_unit_sword_icon.png"
combat_unit_lb_low = "combat_unit_lb_low.png"
combat_unit_esp_low = "combat_unit_esp_low.png"
combat_unit_right_of_icon = "combat_unit_left_of_icon.png"
combat_unit_scroll_area = "combat_unit_scroll_bar.png"

def waitForNextPage(nextPage):
    print "waiting for interstitial page to go away"
    reg.highlight(1)
    if not reg.waitVanish(interstitial_page, FOREVER):
        print "timed out waiting for interstitial page to go away"
    reg.highlight(1)
    if not reg.wait(nextPage, 2.0):
        print "faild to find next page"
ABILITIES = 'save party abilities'
ARENA = 'arena'
RAID = 'raid'
options = (ABILITIES, ARENA, RAID)
selection = select("What do you want to do?", options = options, default = ABILITIES)

print selection
if selection == ABILITIES:
    top = reg.find(combat_group_top)
    bot = reg.find(combat_group_bottom)
    x = top.x
    y = top.y + top.h
    w = top.w
    h = bot.y - y
    active_region = Region(x, y, w, h)
    #active_region.highlight(0.2)
    unit_width = active_region.w/2
    unit_height = active_region.h/3
    units = []
    for row in range(3):
        for col in range(2):
            units.append( Region( x + unit_width * col,
                                  y + unit_height * row,
                                  unit_width,
                                  unit_height
            ))
    print units
    for index, unit in enumerate(units):
        screen.capture(unit).save(tmpdir, "unit-%i.png" % index)
        c = unit.getCenter() # move to right
        unit.mouseMove(c)
        unit.mouseDown(Button.LEFT)
        unit.mouseMove(c.offset(unit_width/2, 0))
        unit.mouseUp(Button.RIGHT)
        ability = 0
        for loc in units:
            screen.capture(unit).save(tmpdir, "unit-%i-ability-%i.png" % (index, ability) )
            ability = ability + 1

    #   0 1
    # 0 1 2
    # 1 3 4
    # 2 5 6

    unit_swords = reg.findAll(combat_group_sword_icon)
    unit_swords_s = sorted(unit_swords, key=lambda t: t.y)
    print "found %i units" % len(unit_swords_s)
elif selection == ARENA:
    if reg.exists(homescreen, 0.001 ):
        print "on homescreen"
        f = find(arena2)
        f.highlight(1)
        f.click()
        waitForNextPage(arena_page)
        if None is reg.exists(arena_page) and None is reg.exists(arena_setup):
            print "failed to reach arena"
            exit
        else:
            print "in arena"
            if reg.exists(arena_has_orb):
                print "arena orb ready"
                reg.click(arena_setup)
                reg.click(arena_rules_ok)
                opponents = reg.findAll(arena_opponent_row)
                opponents_y = sorted(opponents, key=lambda m: m.y)
                l = len(opponents_y)
                print "found %i opponents" % l
                if l > 1:
                    first = opponents_y[0]
                    last = opponents_y[-1]
                    screen.capture(first).save(tmpdir, "arena-first.png")
                    print last.mouseDown(Button.LEFT)
                    print last.mouseMove(first)
                    print first.mouseUp(Button.LEFT)
                    screen.capture(first).save(tmpdir, "arena-first-after-scroll.png")
                    #reg.click(first.getTarget())
    else:
        print "not on homescreen"
        count = 0
        while not reg.exists(homescreen) and count < 10:
            reg.click(back_button)
        print "on homescreen"

elif selection == RAID:
    if reg.exists(raid_event, 0.001 ):
        if reg.exists(raid_event_has_orb):
            print "raid orb ready"
else:
    print "Uknown selection"
