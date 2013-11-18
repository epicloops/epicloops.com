CC_10_MINS=600
CC_10_YEARS=315360000
#==============================================================================
# HTML
#==============================================================================
aws s3 sync ./output s3://epicloops.com/ \
--exclude "*" \
--include "*.html" \
--content-encoding "gzip" \
--cache-control "public, max-age=$CC_10_MINS" \
--acl "public-read" \
--delete

#==============================================================================
# XML
#==============================================================================
aws s3 sync ./output s3://epicloops.com/ \
--exclude "*" \
--include "*.xml" \
--content-encoding "gzip" \
--cache-control "public, max-age=$CC_10_MINS" \
--acl "public-read" \
--delete

#==============================================================================
# TXT
#==============================================================================
aws s3 sync ./output s3://epicloops.com/ \
--exclude "*" \
--include "*.txt" \
--cache-control "public, max-age=$CC_10_MINS" \
--acl "public-read" \
--delete

#==============================================================================
# CSS
#==============================================================================
aws s3 sync ./output s3://epicloops.com/ \
--exclude "*" \
--include "*.css" \
--content-encoding "gzip" \
--cache-control "public, max-age=$CC_10_YEARS" \
--acl "public-read" \
--delete

#==============================================================================
# JPG
#==============================================================================
aws s3 sync ./output s3://epicloops.com/ \
--exclude "*" \
--include "*.jpg" \
--cache-control "public, max-age=$CC_10_YEARS" \
--acl "public-read" \
--delete

#==============================================================================
# PNG
#==============================================================================
aws s3 sync ./output s3://epicloops.com/ \
--exclude "*" \
--include "*.png" \
--cache-control "public, max-age=$CC_10_YEARS" \
--acl "public-read" \
--delete

#==============================================================================
# FONT
#==============================================================================
aws s3 sync ./output/static/font s3://epicloops.com/static/font \
--content-encoding "gzip" \
--cache-control "public, max-age=$CC_10_YEARS" \
--acl "public-read" \
--delete
