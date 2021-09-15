from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker


def index(request):
    context = {
        "leagues": League.objects.all(),
        "teams": Team.objects.all(),
        "players": Player.objects.all(),
        # "baseball_leagues": League.objects.filter(sport="Baseball"),
        "baseball_leagues": League.objects.filter(sport__contains="baseball"),
        "women_leagues": League.objects.filter(name__contains="women"),
        "all_hockey_leagues": League.objects.filter(sport__contains="hockey"),
        "not_football_leagues": League.objects.exclude(sport__contains="football"),
        "conferences_leagues": League.objects.filter(name__contains="conference"),
        "all_league_atlantic": League.objects.filter(name__contains="atlantic"),
        "teams_house_dallas": Team.objects.filter(location__contains="dallas"),
        "teams_with_raptors": Team.objects.filter(team_name__contains="raptors"),
        "teams_with_city": Team.objects.filter(location__contains="city"),
        "teams_startswith_t": Team.objects.filter(team_name__startswith="T"),
        "teams_orderby_location": Team.objects.all().order_by("location"),
        "teams_orderby_name": Team.objects.all().order_by("-team_name"),
        "player_lastname_cooper": Player.objects.filter(last_name__contains="cooper"),
        "player_name_joshua": Player.objects.filter(first_name__contains="joshua"),
        "player_cooper_less_joshua": Player.objects.filter(last_name__contains="cooper").exclude(first_name__contains="joshua"),
        "player_name_alexander_or_wyatt": Player.objects.filter(first_name__in=["Alexander", "Wyatt"]),
    }
    return render(request, "leagues/index.html", context)


def index2(request):
    context = {
        "leagues": League.objects.all(),
        "teams": Team.objects.all(),
        "players": Player.objects.all(),
        # 1
        "teams_atlantic_soccer_conference": Team.objects.filter(league__name__contains="atlantic soccer conference"),
        # 2
        "players_boston_penguins": Player.objects.filter(curr_team__location="Boston", curr_team__team_name="Penguins"),
        # 3
        "players_in_ICBC": Player.objects.filter(curr_team__league__name="International Collegiate Baseball Conference"),
        # 4
        "players_CAFA_lopez": Player.objects.filter(curr_team__league__name="American Conference of Amateur Football").filter(last_name__contains="lopez"),
        # 5
        "football_players": Player.objects.filter(curr_team__league__sport__contains="football"),
        # 6
        "teams_with_sophia": Player.objects.filter(first_name="Sophia"),
        # 7
        "leagues_with_sophia": Player.objects.filter(first_name="Sophia"),
        # 8
        "players_notWR_flores": Player.objects.filter(last_name="Flores").exclude(curr_team__team_name="Roughriders", curr_team__location="Washington"),
        # 9
        "teams_Samuel_Evans": Player.objects.get(first_name="Samuel", last_name="Evans").all_teams.all(),
        # 10
        "players_in_MTC": Player.objects.filter(all_teams__team_name="Tiger-Cats", all_teams__location="Manitoba"),
        # 11
        "ex_players_WV": Player.objects.filter(all_teams__team_name="Vikings", all_teams__location="Wichita").exclude(curr_team__team_name="Vikings"),
        # 12
        "jacob_gray_ex_teams": Player.objects.get(first_name="Jacob", last_name="Gray").all_teams.all().exclude(team_name="Colts", location="Oregon"),
        # 13
        "all_joshuas_in_AFABP": Player.objects.filter(first_name="Joshua", all_teams__league__name="Atlantic Federation of Amateur Baseball Players"),


    }
    return render(request, "leagues/index2.html", context)


def make_data(request):
    team_maker.gen_leagues(10)
    team_maker.gen_teams(50)
    team_maker.gen_players(200)

    return redirect("index")
