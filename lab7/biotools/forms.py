from django import forms


class SeqContentForm(forms.Form):
	sequence = forms.CharField(
		widget=forms.Textarea(attrs={
			'placeholder': 'Plain sequence',
			'class': 'form-control'
			}),
		min_length=5,
		required=True)
	word_size = forms.IntegerField(
		initial=1,
		widget=forms.TextInput(attrs={'class': 'form-control'}),
		required=True
	)


	def clean_sequence(self):
		sequence = self.cleaned_data['sequence']
		return sequence.upper()

	def clean_word_size(self):
		word_size = self.cleaned_data['word_size']
		if word_size < 1:
			raise forms.ValidationError('Word size must be >= 1')
		return word_size

	def clean(self):
		sequence = self.cleaned_data.get('sequence')
		word_size = self.cleaned_data.get('word_size')
        # Only do something if both fields are valid so far
		if sequence and word_size:
			if len(sequence) < word_size:
				raise forms.ValidationError('Sequence cannot be shorter than word size')