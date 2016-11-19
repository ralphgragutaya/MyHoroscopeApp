from django import forms

class HoroscopeForm(forms.Form):
    zodiac_sign = forms.ChoiceField(
        label = 'Zodiac Sign',
        widget = forms.Select(),
        choices =([
            ('aquarius', 'Jan 20 - Feb 18 = Aquarius'),
            ('pisces', 'Feb 19 - Mar 20 = Pisces'),
            ('aries', 'Mar 21 - Apr 19 = Aries'),
            ('taurus', 'Apr 20 - May 20 = Taurus'),
            ('gemini', 'May 21 - Jun 20 = Gemini'),
            ('cancer', 'Jun 21 - Jul 22 = Cancer'),
            ('leo', 'Jul 23 - Aug 22 = Leo'),
            ('virgo', 'Aug 23 - Sep 22 = Virgo'),
            ('libra', 'Sep 23 - Oct 22 = Libra'),
            ('scorpio', 'Oct 23 - Nov 21 = Scorpio'),
            ('sagitarius', 'Nov 22 - Dec 21 = Sagitarius'),
            ('capricorn', 'Dec 22 - Jan 19 = Capricorn'),
        ]),
    )

    period = forms.ChoiceField(
        label = 'Period',
        widget = forms.Select(),
        choices = ([
            ('today', 'Today'),
            ('week', 'Week'),
            ('month', 'Month'),
            ('year', 'Year'),
        ]),
    )
