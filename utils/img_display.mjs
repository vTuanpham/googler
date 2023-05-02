import terminalImage from 'terminal-image';
import got from 'got';

export async function display_img(url, size, opts) {
    if (opts['method'] == 'open image from web') {
        const body = await got(url).buffer();
        console.log(await terminalImage.buffer(body, {width: size, height: size, preserveAspectRatio: true}));
    }
    if (opts['method'] == 'load saved svg image') {
        console.log(await terminalImage.file(url, {width: size, height: size, preserveAspectRatio: true}));
    }
}

