from os import walk
from shutil import copyfile
from __builtin__ import staticmethod

class FontAwesome3To4:
    FA_ICONS = {
        'icon-ban-circle': 'fa-ban',
        'icon-bar-chart': 'fa-bar-chart-o',
        'icon-beaker': 'fa-flask',
        'icon-bell': 'fa-bell-o',
        'icon-bell-alt': 'fa-bell',
        'icon-bitbucket-sign': 'fa-bitbucket-square',
        'icon-bookmark-empty': 'fa-bookmark-o',
        'icon-building': 'fa-building-o',
        'icon-calendar-empty': 'fa-calendar-o',
        'icon-check-empty': 'fa-square-o',
        'icon-check-minus': 'fa-minus-square-o',
        'icon-check-sign': 'fa-check-square',
        'icon-check': 'fa-check-square-o',
        'icon-chevron-sign-down': 'fa-chevron-circle-down',
        'icon-chevron-sign-left': 'fa-chevron-circle-left',
        'icon-chevron-sign-right': 'fa-chevron-circle-right',
        'icon-chevron-sign-up': 'fa-chevron-circle-up',
        'icon-circle-arrow-down': 'fa-arrow-circle-down',
        'icon-circle-arrow-left': 'fa-arrow-circle-left',
        'icon-circle-arrow-right': 'fa-arrow-circle-right',
        'icon-circle-arrow-up': 'fa-arrow-circle-up',
        'icon-circle-blank': 'fa-circle-o',
        'icon-cny': 'fa-rub',
        'icon-collapse-alt': 'fa-minus-square-o',
        'icon-collapse-top': 'fa-caret-square-o-up',
        'icon-collapse': 'fa-caret-square-o-down',
        'icon-comment-alt': 'fa-comment-o',
        'icon-comments-alt': 'fa-comments-o',
        'icon-copy': 'fa-files-o',
        'icon-cut': 'fa-scissors',
        'icon-dashboard': 'fa-tachometer',
        'icon-double-angle-down': 'fa-angle-double-down',
        'icon-double-angle-left': 'fa-angle-double-left',
        'icon-double-angle-right': 'fa-angle-double-right',
        'icon-double-angle-up': 'fa-angle-double-up',
        'icon-download': 'fa-arrow-circle-o-down',
        'icon-download-alt': 'fa-download',
        'icon-edit-sign': 'fa-pencil-square',
        'icon-edit': 'fa-pencil-square-o',
        'icon-ellipsis-horizontal': 'fa-ellipsis-h',
        'icon-ellipsis-vertical': 'fa-ellipsis-v',
        'icon-envelope-alt': 'fa-envelope-o',
        'icon-exclamation-sign': 'fa-exclamation-circle',
        'icon-expand-alt': 'fa-expand-o',
        'icon-expand': 'fa-caret-square-o-right',
        'icon-external-link-sign': 'fa-external-link-square',
        'icon-eye-close': 'fa-eye-slash',
        'icon-eye-open': 'fa-eye',
        'icon-facebook-sign': 'fa-facebook-square',
        'icon-facetime-video': 'fa-video-camera',
        'icon-file-alt': 'fa-file-o',
        'icon-file-text-alt': 'fa-file-text-o',
        'icon-flag-alt': 'fa-flag-o',
        'icon-folder-close-alt': 'fa-folder-o',
        'icon-folder-close': 'fa-folder',
        'icon-folder-open-alt': 'fa-folder-open-o',
        'icon-food': 'fa-cutlery',
        'icon-frown': 'fa-frown-o',
        'icon-fullscreen': 'fa-arrows-alt',
        'icon-github-sign': 'fa-github-square',
        'icon-google-plus-sign': 'fa-google-plus-square',
        'icon-group': 'fa-users',
        'icon-h-sign': 'fa-h-square',
        'icon-hand-down': 'fa-hand-o-down',
        'icon-hand-left': 'fa-hand-o-left',
        'icon-hand-right': 'fa-hand-o-right',
        'icon-hand-up': 'fa-hand-o-up',
        'icon-hdd': 'fa-hdd-o (4.0.1)',
        'icon-heart-empty': 'fa-heart-o',
        'icon-hospital': 'fa-hospital-o',
        'icon-indent-left': 'fa-outdent',
        'icon-indent-right': 'fa-indent',
        'icon-info-sign': 'fa-info-circle',
        'icon-keyboard': 'fa-keyboard-o',
        'icon-legal': 'fa-gavel',
        'icon-lemon': 'fa-lemon-o',
        'icon-lightbulb': 'fa-lightbulb-o',
        'icon-linkedin-sign': 'fa-linkedin-square',
        'icon-meh': 'fa-meh-o',
        'icon-microphone-off': 'fa-microphone-slash',
        'icon-minus-sign-alt': 'fa-minus-square',
        'icon-minus-sign': 'fa-minus-circle',
        'icon-mobile-phone': 'fa-mobile',
        'icon-moon': 'fa-moon-o',
        'icon-move': 'fa-arrows',
        'icon-off': 'fa-power-off',
        'icon-ok-circle': 'fa-check-circle-o',
        'icon-ok-sign': 'fa-check-circle',
        'icon-ok': 'fa-check',
        'icon-paper-clip': 'fa-paperclip',
        'icon-paste': 'fa-clipboard',
        'icon-phone-sign': 'fa-phone-square',
        'icon-picture': 'fa-picture-o',
        'icon-pinterest-sign': 'fa-pinterest-square',
        'icon-play-circle': 'fa-play-circle-o',
        'icon-play-sign': 'fa-play-circle',
        'icon-plus-sign-alt': 'fa-plus-square',
        'icon-plus-sign': 'fa-plus-circle',
        'icon-pushpin': 'fa-thumb-tack',
        'icon-question-sign': 'fa-question-circle',
        'icon-remove-circle': 'fa-times-circle-o',
        'icon-remove-sign': 'fa-times-circle',
        'icon-remove': 'fa-times',
        'icon-reorder': 'fa-bars',
        'icon-resize-full': 'fa-expand',
        'icon-resize-horizontal': 'fa-arrows-h',
        'icon-resize-small': 'fa-compress',
        'icon-resize-vertical': 'fa-arrows-v',
        'icon-rss-sign': 'fa-rss-square',
        'icon-save': 'fa-floppy-o',
        'icon-screenshot': 'fa-crosshairs',
        'icon-share-alt': 'fa-share',
        'icon-share-sign': 'fa-share-square',
        'icon-share': 'fa-share-square-o',
        'icon-sign-blank': 'fa-square',
        'icon-signin': 'fa-sign-in',
        'icon-signout': 'fa-sign-out',
        'icon-smile': 'fa-smile-o',
        'icon-sort-by-alphabet-alt': 'fa-sort-alpha-desc',
        'icon-sort-by-alphabet': 'fa-sort-alpha-asc',
        'icon-sort-by-attributes-alt': 'fa-sort-amount-desc',
        'icon-sort-by-attributes': 'fa-sort-amount-asc',
        'icon-sort-by-order-alt': 'fa-sort-numeric-desc',
        'icon-sort-by-order': 'fa-sort-numeric-asc',
        'icon-sort-down': 'fa-sort-asc',
        'icon-sort-up': 'fa-sort-desc',
        'icon-stackexchange': 'fa-stack-overflow',
        'icon-star-empty': 'fa-star-o',
        'icon-star-half-empty': 'fa-star-half-o',
        'icon-sun': 'fa-sun-o',
        'icon-thumbs-down-alt': 'fa-thumbs-o-down',
        'icon-thumbs-up-alt': 'fa-thumbs-o-up',
        'icon-time': 'fa-clock-o',
        'icon-trash': 'fa-trash-o',
        'icon-tumblr-sign': 'fa-tumblr-square',
        'icon-twitter-sign': 'fa-twitter-square',
        'icon-unlink': 'fa-chain-broken',
        'icon-upload': 'fa-arrow-circle-o-up',
        'icon-upload-alt': 'fa-upload',
        'icon-warning-sign': 'fa-exclamation-triangle',
        'icon-xing-sign': 'fa-xing-square',
        'icon-youtube-sign': 'fa-youtube-square',
        'icon-zoom-in': 'fa-search-plus',
        'icon-zoom-out': 'fa-search-minus'
    }
    
    FA_ICONS_NOFA = {
        'icon-large': 'fa-lg',
        'icon-2x': 'fa-2x',
        'icon-3x': 'fa-3x',
        'icon-4x': 'fa-4x',
        'icon-border': 'fa-border',
        'icons-ul': 'fa-ul',
        'icon-li': 'fa-li',
        'icon-fixed-width': 'fa-fw',
        'icon-spin': 'fa-spin',
        'icon-rotate-90': 'fa-rotate-90',
        'icon-rotate-180': 'fa-rotate-180',
        'icon-rotate-270': 'fa-rotate-270',
        'icon-flip-horizontal': 'fa-flip-horizontal',
        'icon-flip-vertical': 'fa-flip-vertical',
        'icon-stack': 'fa-stack',
        'icon-stack-base': 'fa-stack-2x',
        'icon-light': 'fa-inverse',
        'icon-muted': '',
    }
    
    @staticmethod
    def pathCheck (dir, createBackup):
        for (dirpath, dirnames, filenames) in walk(dir):
            for filename in filenames:
                FontAwesome3To4.fileCheck(dir+'/'+filename, createBackup)
            break
        
    @staticmethod
    def fileCheck (fullpath, createBackup):
        if (fullpath[-3:] == "bak"):
            return
        
        if (createBackup):
            copyfile(fullpath, fullpath+'.bak')
        
        with open(fullpath, 'r+') as file:
            content = file.read()
            file.seek(0)
            for attribute, value in FontAwesome3To4.FA_ICONS.iteritems():
                content = content.replace(attribute, 'fa '+value)
            for attribute, value in FontAwesome3To4.FA_ICONS_NOFA.iteritems():
                content = content.replace(attribute, value)
            content = content.replace('icon-', 'fa fa-')
            
            stackCount = content.count('fa-stack')
            if (stackCount > 0):
                print str(stackCount)+" STACKED ICONS in "+fullpath+", please review these icons manually"
            
            file.write(content)