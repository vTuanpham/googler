import pkg from 'terminal-kit';
const { terminal: term } = pkg;


export async function generate_text(text, delay_in_ms) {
  term.slowTyping(
    text+'\n',
    { flashStyle: term.brightWhite, delay: delay_in_ms },
	function() {}
) ;
}

