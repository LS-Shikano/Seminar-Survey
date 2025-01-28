from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    currency_range,
)
import random 

author = 'group 2'
doc = 'Goal: social movement'

class Constants(BaseConstants):
    name_in_url = 'survey-group2'
    players_per_group = None
    num_rounds = 1
    
class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
        framing = models.StringField(choices=['positive', 'negative', 'neutral'])
    

class Player(BasePlayer):
    time_start = models.StringField(initial="-999")
    
    # Keep political attributes in Pretest or move to Demographics?
    eco_poli_affiliation = models.IntegerField(
        label="<b>Wie ist Ihre politische Ausrichtung in Bezug auf die Wirtschaft?</b> <i>(1: Umverteilung, Sozialistisch - 10: Konservativ, offene Märkte)</i>",
        choices=[(1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10')],
        widget=widgets.RadioSelectHorizontal,
    )
    soci_poli_affiliation = models.IntegerField(
        label="<b>Wie ist Ihre politische Ausrichtung in Bezug auf gesellschaftliche Themen?</b> <i>(1: Liberal bezüglich Lebensstile & Kulturen - 10: Konservativ, traditionelle Familienwerte)</i>",
        choices=[(1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10')],
        widget=widgets.RadioSelectHorizontal,
    )
    
    # Pre-Treatment 
    concept_freetrade = models.IntegerField(
        label="Wie vertraut sind Sie mit dem Konzept von Freihandelsabkommen? (1: Überhaupt nicht vertraut - 10: Sehr vertraut)",
        choices=[(1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10')],
        widget=widgets.RadioSelectHorizontal,
    )

    mercosur_freetrade = models.IntegerField(
        label="Wie vertraut sind Sie mit dem Mercosur-Freihandelsabkommen? (1: Überhaupt nicht vertraut - 10: Sehr vertraut)",
        choices=[(1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10')],
        widget=widgets.RadioSelectHorizontal,
    )

    supportive_freetrade = models.IntegerField(
        label="Wie unterstützend stehen Sie im Allgemeinen Freihandelsabkommen gegenüber? (1: Keine Unterstüzung - 10: Volle Unterstüzung)",
        choices=[(1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10')],
        widget=widgets.RadioSelectHorizontal,
    )

    trust_government = models.IntegerField(
        label="Wie sehr vertrauen Sie der Regierung, faire Handelsabkommen auszuhandeln? (1: Kein Vertrauen - 10: Volles Vertrauen)",
        choices=[(1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10')],
        widget=widgets.RadioSelectHorizontal,
    )

    trust_media = models.IntegerField(
        label="Wie sehr vertrauen Sie der Medienberichterstattung über internationale Handelsabkommen? (1: Kein Vertrauen - 10: Volles Vertrauen)",
        choices=[(1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10')],
        widget=widgets.RadioSelectHorizontal,
    )

    
    pre_talk_friends = models.BooleanField(
        label="• Mit Freunden oder der Familie darüber gesprochen:",
        choices=[
            [True, "Ja"],
            [False, "Nein"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    pre_share_socialmedia = models.BooleanField(
        label="• Ihre Meinung in sozialen Medien geteilt:",
        choices=[
            [True, "Ja"],
            [False, "Nein"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    pre_consider_voting = models.BooleanField(
        label="• Die Haltung eines Kandidaten bei Wahlen berücksichtigt:",
        choices=[
            [True, "Ja"],
            [False, "Nein"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    pre_support_petition = models.BooleanField(
        label="• Eine Online-Petition unterstützt:",
        choices=[
            [True, "Ja"],
            [False, "Nein"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    pre_attend_protest = models.BooleanField(
        label="• An einer Demonstration oder einem Protest teilgenommen:",
        choices=[
            [True, "Ja"],
            [False, "Nein"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    pre_legal_action = models.BooleanField(
        label="• Rechtliche Schritte etwa in Form einer Sammelklage eingeleitet:",
        choices=[
            [True, "Ja"],
            [False, "Nein"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

# Framing Treatment Page
    #assigned_treatment = models.StringField()
    treatment = models.StringField()
    time_popout = models.StringField(initial='-999',blank=True)

    select_proceed = models.BooleanField(
    blank=False,
    label="Um zu bestätigen das Sie den Text gelesen haben, wählen Sie bitte 'Nein' aus.", #to be changed not a fan of this type of question 
    choices=[
        [True, "Ja"],
        [False, "Nein"]
    ],
    widget=widgets.RadioSelectHorizontal
    )


#manipulation checks page
    describe_tone = models.IntegerField(
        label="Wie würden Sie den Ton der Beschreibung des Mercosur-Abkommens einschätzen, die Sie zuvor gelesen haben? (1: Sehr negativ - 10: Sehr positiv)",
        choices=[(1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10')],
        widget=widgets.RadioSelectHorizontal
    )

    mentioned_points_1 = models.IntegerField(blank=True, max=2, min=1, label="")
    mentioned_points_2 = models.IntegerField(blank=True, max=2, min=1, label="")
    mentioned_points_3 = models.IntegerField(blank=True, max=2, min=1, label="")
    mentioned_points_4 = models.IntegerField(blank=True, max=2, min=1, label="")
    
    overall_message = models.StringField(
        label="Was war die allgemeine Botschaft der Beschreibung, die Sie über das Mercosur-Abkommen gelesen haben?",
        choices=[(1,"Das Abkommen wurde positiv dargestellt."), 
                 (2,"Das Abkommen wurde negativ dargestellt."), 
                 (3,"Das Abkommen wurde neutral dargestellt."), 
                 (4,"Ich bin mir nicht sicher.")],
        widget=widgets.RadioSelect,
    )
    
# posttreatment page
    supportive_mercosur = models.IntegerField(
        label="Nach dem Lesen dieser Beschreibung, wie unterstützend stehen Sie dem Mercosur-Abkommen gegenüber? (1: Nicht unterstützend - 10: Sehr unterstützend)",
        choices=[(1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10')],
        widget=widgets.RadioSelectHorizontal,
    )

    relevant_mercosur = models.IntegerField(
        label="Wie relevant erscheint Ihnen persönlich das Mercosur-Abkommen? (1: Nicht relevant - 10: Sehr relevant)",
        choices=[(1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10')],
        widget=widgets.RadioSelectHorizontal,
    )  

    # concerns_mercosur = models.StringField(
    #     label="Was bereitet Ihnen am meisten Sorgen im Zusammenhang mit dem Mercosur-Abkommen? (Wählen Sie bis zu 2 aus)",
    #     blank=True,
    #     choices=[(1, 'Potenzieller Schaden für lokale Landwirte und Unternehmen in der EU.'),
    #         (2, 'Wirtschaftliche Instabilität für gefährdete Sektoren.'),
    #         (3, 'Erhöhte Abhängigkeit von ausländischen Importen.'),
    #         (4, 'Risiko unzureichender Durchsetzung von Regulierungsstandards.')],
    #     widget=widgets.RadioSelect,
    # )
    concerns_mercosur_1 = models.IntegerField(blank=True, max=2, min=1, label="")
    concerns_mercosur_2 = models.IntegerField(blank=True, max=2, min=1, label="")
    concerns_mercosur_3 = models.IntegerField(blank=True, max=2, min=1, label="")
    concerns_mercosur_4 = models.IntegerField(blank=True, max=2, min=1, label="")
    other_concerns_mercosur = models.StringField(blank=True, label="Sonstiges(bitte angeben):")
   
    # positive_impact_mercosur = models.StringField(
    #     label="4- Was halten Sie für die positivste Auswirkung des Mercosur-Abkommens? (Wählen Sie bis zu 2 aus)",
    #     blank=True,
    #     choices=[(1,"Geringere Kosten für Verbraucher durch reduzierte Zölle."),
    #         (2,"Stärkere internationale Handelsbeziehungen."),
    #         (3,"Potenzielles Wirtschaftswachstum in beiden Regionen."),
    #         (4,"Erhöhte Exportmöglichkeiten für europäische Unternehmen.")],
    #     widget=widgets.RadioSelect 
    # )
    positive_impact_mercosur_1 = models.IntegerField(blank=True, max=2, min=1, label="")
    positive_impact_mercosur_2 = models.IntegerField(blank=True, max=2, min=1, label="")
    positive_impact_mercosur_3 = models.IntegerField(blank=True, max=2, min=1, label="")
    positive_impact_mercosur_4 = models.IntegerField(blank=True, max=2, min=1, label="")
    other_positive_impact_mercosur = models.StringField(blank=True, label="Sonstiges(bitte angeben):")

    # aspect_mercosur = models.StringField(
    #     label="5- Welcher Aspekt des Mercosur-Abkommens erfordert Ihrer Meinung nach die größte Aufmerksamkeit? (Wählen Sie bis zu 2 aus)",
    #     blank=True,
    #     choices=[(1,"Sicherstellung eines fairen Wettbewerbs für lokale Industrien."),
    #         (2,"Unterstützung der Arbeitsplatzsicherheit in betroffenen Sektoren."),
    #         (3,"Aufrechterhaltung hoher regulatorischer und Sicherheitsstandards."),
    #         (4,"Ausgewogenheit zwischen kurzfristigen wirtschaftlichen Gewinnen und langfristigen Auswirkungen.")],
    #     widget=widgets.RadioSelect        
    # )
    aspect_mercosur_1 = models.IntegerField(blank=True, max=2, min=1, label="")
    aspect_mercosur_2 = models.IntegerField(blank=True, max=2, min=1, label="")
    aspect_mercosur_3 = models.IntegerField(blank=True, max=2, min=1, label="")
    aspect_mercosur_4 = models.IntegerField(blank=True, max=2, min=1, label="")
    other_aspect_mercosur = models.StringField(blank=True, label="Sonstiges(bitte angeben):)")

    #Wie wahrscheinlich ist es, dass Sie eine der folgenden Handlungen durchführen in Bezug auf das Mercosur Handelsabkommen?
    post_talk_friends = models.IntegerField(
        label="• Mit Freunden oder der Familie darüber sprechen: (1: Sehr Unwahrscheinlich - 10: Sehr wahrscheinlich)" ,
        choices=[(1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10')],
        widget=widgets.RadioSelectHorizontal
    )
    post_share_socialmedia = models.IntegerField(
        label="• Ihre Meinung in sozialen Medien teilen: (1: Sehr Unwahrscheinlich - 10: Sehr wahrscheinlich)",
        choices=[(1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10')],
        widget=widgets.RadioSelectHorizontal
    )
    
    post_consider_voting = models.IntegerField(
        label="• Die Haltung eines Kandidaten bei Wahlen berücksichtigen: (1: Sehr Unwahrscheinlich - 10: Sehr wahrscheinlich)",
        choices=[(1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10')],
        widget=widgets.RadioSelectHorizontal
    )
    post_support_petition = models.IntegerField(
        label="Eine Online-Petition unterstützten: (1: Sehr Unwahrscheinlich - 10: Sehr wahrscheinlich)",
        choices=[(1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10')],
        widget=widgets.RadioSelectHorizontal
    )
    post_attend_protest = models.IntegerField(
        label="An einer Demonstration oder einem Protest teilnehmen: <i>(1: Sehr Unwahrscheinlich - 10: Sehr wahrscheinlich)</i>",
        choices=[(1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10')],
        widget=widgets.RadioSelectHorizontal
    )
    post_legal_action = models.IntegerField(
        label="Rechtliche Schritte etwa in Form einer Sammelklage einleiten: <i>(1: Sehr Unwahrscheinlich - 10: Sehr wahrscheinlich)</i>",
        choices=[(1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10')],
        widget=widgets.RadioSelectHorizontal
    )
    

    
