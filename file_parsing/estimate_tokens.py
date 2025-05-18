def estimate_tokens(prompt_body: str):
    return len(prompt_body.split(' '))


def warn_excession(num_tokens):
    MAX_NUM_TOKENS = 32000
    
    if num_tokens >= MAX_NUM_TOKENS:    
        print(f'The number of tokens of your prompt has will exceed the maximum window length.',
              'You might want to consider breaking your query up into smaller parts, or parsing smaller folders')
        return